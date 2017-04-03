# generate network equivalent to generic test-mh
# 3 participants
# combination of inbound and outbound rules
# additional test for unmatched traffic on port 8888

mode multi-hop
participants 3
peers 1 2 3

participant 1 100 edge-1:5 MAC 172.0.0.1/16
participant 2 200 edge-2:5 MAC 172.0.0.11/16
participant 3 300 edge-3:5 MAC 172.0.0.21/16 edge-4:5 MAC 172.0.0.22/16

host AS ROUTER _ IP           # host names of form a1_100 a1_110

announce 1 100.0.0.0/24 110.0.0.0/24
announce 2 120.0.0.0/24 130.0.0.0/24
announce 3 140.0.0.0/24 150.0.0.0/24


flow a1 80 >> c
flow a1 443 >> c
flow b1 80 >> c
flow c1 << 80
flow c1 << 443
flow c1 1 | a1 ipv4_dst=140.0.0.1 udp_dst=443
flow c1 2 | a1 ipv4_dst=140.0.0.2 udp_dst=80
flow c1 3 | b1 ipv4_dst=140.0.0.1 udp_dst=80

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {
	delay 5
	test xfer
	delay 5
#start all send
	test start_all_send
	delay 5
    test show_table_2
    test delay
#insert 1
	blackholing 3 insert 1
	delay 5
	test show_table_2
	test delay
#insert 2
    blackholing 3 insert 2
    delay 5
    test show_table_2
    test delay
#insert 3
	blackholing 3 insert 3
	delay 5
	test show_table_2
	test delay
#stop restart send
	test stop_restart_send
	delay 5
	test show_table_2
	test delay
#remove all
	blackholing 3 remove 1,2,3
	test delay
#stop all send
	test stop_all_send
	test delay
	test delay
	test info
}

test xfer {
	verify a1_100 c1_140 8888
	verify b1_120 c1_140 8888
	verify a1_100 b1_120 8888
}

test show_table_2 {
    local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=3
    local ovs-ofctl dump-flows edge-2 -O OpenFlow13 table=3
}

test delay {
	delay 50
}

test start_all_send {
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -u -t 420 -b 20M &IPERF_P1
    test start_restart_send
}

test start_restart_send {
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 443 -u -t 420 -b 30M &IPERF_B1
    exec a1_100 iperf -c 140.0.0.2 -B 100.0.0.1 -p 80 -u -t 420 -b 40M &IPERF_B2
    exec b1_120 iperf -c 140.0.0.1 -B 120.0.0.1 -p 80 -u -t 420 -b 50M &IPERF_B3
}

test stop_restart_send {
	killp a1_100 IPERF_B1
	killp a1_100 IPERF_B2
	killp b1_120 IPERF_B3
}

test stop_all_send {
	killp a1_100 IPERF_P1
	test stop_restart_send
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec b1 ip route
}

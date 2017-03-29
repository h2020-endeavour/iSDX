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

flow a1 8080 >> c
flow b1 8080 >> c
flow c1 << 8080
flow c1 1 | a1 ipv4_dst=140.0.0.1 tcp_dst=8080
flow c1 2 | a1 ipv4_dst=140.0.0.2 tcp_dst=8080
flow c1 3 | b1 ipv4_dst=140.0.0.3 tcp_dst=8080
flow c1 4 | b1 ipv4_dst=140.0.0.4 tcp_dst=8080

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {
	test delay
	test start_log
	test delay
	test xfer
	test delay
	comment comment-0
	test show_table_2
	test start_first_send
	test delay
	api 3 insert static_routes
	test delay
	test show_table_2
	test stop_log
	test delay
}



test xfer {
	verify a1_100 c1_140 8888
	verify b1_120 c1_140 8888
	verify a1_100 b1_120 8888
}

test show_table_2 {
    local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=3
    comment comment-end
}

test delay {
	delay 40
}

test start_log {
	test stop_log
	exec c1_140 ifconfig c1_140-eth0:0 140.0.0.2
	exec c1_140 ifconfig c1_140-eth0:1 140.0.0.3
	exec c1_140 ifconfig c1_140-eth0:2 140.0.0.4
	delay 5
    exec c1_140 iperf3 -s -B 140.0.0.1 -p 8080 --logfile iperf3_bh-test1.log &IPERF_1
    exec c1_140 iperf3 -s -B 140.0.0.2 -p 8080 --logfile iperf3_bh-test2.log &IPERF_2
    exec c1_140 iperf3 -s -B 140.0.0.3 -p 8080 --logfile iperf3_bh-test3.log &IPERF_3
    exec c1_140 iperf3 -s -B 140.0.0.4 -p 8080 --logfile iperf3_bh-test4.log &IPERF_4
}

test start_first_send {
    exec b1_120 iperf3 -c 140.0.0.4 -B 120.0.0.1 -p 8080 -t 500 -b 100M &IPERF_B4
}

test cycle_0 {
    blackholing 3 insert 4
    test delay
    blackholing 3 remove 2
    delay 5
    killps a1_100 IPERF_B2
    test delay
    exec a1_100 iperf3 -c 140.0.0.1 -B 100.0.0.1 -p 8080 -t 500 -b 100M &IPERF_B1
}

test cycle_1 {
	blackholing 3 insert 1
    test delay
    blackholing 3 remove 3
    delay 5
    killps b1_120 IPERF_B3
    test delay
    exec a1_100 iperf3 -c 140.0.0.2 -B 100.0.0.1 -p 8080 -t 500 -b 100M &IPERF_B2
}

test cycle_2 {
	blackholing 3 insert 2
	test delay
	blackholing 3 remove 4
	delay 5
	killps b1_120 IPERF_B4
	test delay
    exec b1_120 iperf3 -c 140.0.0.3 -B 120.0.0.1 -p 8080 -t 500 -b 100M &IPERF_B3
}

test cycle_3 {
	blackholing 3 insert 3
	test delay

	test show_table_2
	
	blackholing 3 remove 1
	delay 5
	killps a1_100 IPERF_B1
	
	test restart_log
	test delay
    exec b1_120 iperf3 -c 140.0.0.4 -B 120.0.0.1 -p 8080 -t 500 -b 100M &IPERF_B4
}

test restart_log {
	test stop_log
	delay 5
	exec c1_140 iperf3 -s -B 140.0.0.1 -p 8080 --logfile iperf3_bh-test1.log &IPERF_1
    exec c1_140 iperf3 -s -B 140.0.0.2 -p 8080 --logfile iperf3_bh-test2.log &IPERF_2
    exec c1_140 iperf3 -s -B 140.0.0.3 -p 8080 --logfile iperf3_bh-test3.log &IPERF_3
    exec c1_140 iperf3 -s -B 140.0.0.4 -p 8080 --logfile iperf3_bh-test4.log &IPERF_4

}

test stop_log {
    killps c1_140 IPERF_1
    killps c1_140 IPERF_2
    killps c1_140 IPERF_3
    killps c1_140 IPERF_4
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec b1 ip route
}

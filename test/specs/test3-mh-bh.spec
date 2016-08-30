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
flow b1 80 >> c
flow c1 << 80
flow c1 << 8888
flow c1 4096 | a1
flow c1 8192 | b1

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {
	delay 5
	test xfer
	test delay
#start
	test start_send
	delay 5
    test show_table_2
    test delay
#insert 1
	blackholing 3 insert 4096
	delay 5
	test show_table_2
	test delay
#insert 2
    blackholing 3 insert 8192
    delay 5
    test show_table_2
    test delay
#remove 1
	blackholing 3 remove 4096
	delay 5
	test show_table_2
	test delay
# remove 2
	blackholing 3 remove 8192
	delay 5
	test show_table_2
	test delay
# insert all
	blackholing 3 insert 4096,8192
	delay 5
	test show_table_2
	blackholing 3 remove 4096,8192
	delay 5
	test show_table_2
	test delay
	test stop_send
	test delay
	test info
}

test xfer {
	verify a1_100 c1_140 8888
	verify b1_120 c1_140 8888
}

test show_table_2 {
    local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
    local ovs-ofctl dump-flows edge-2 -O OpenFlow13 table=2
}

test delay {
	delay 40
}

test start_send {
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -u -t 350 -b 50M &IPERF1
    delay 40
    exec b1_120 iperf -c 140.0.0.1 -B 120.0.0.1 -p 80 -u -t 350 -b 70M &IPERF1
}

test stop_send {
	killp a1_100 IPERF1
	killp b1_120 IPERF1
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec b1 ip route
}

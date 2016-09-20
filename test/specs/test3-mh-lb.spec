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

flow a1 80 >> b
flow a1 80 >> c
flow b1 80 >> c
flow c1 << 80

listener AUTOGEN 8888

test init {
	listener
}

test regress {
	delay 5
#start all send
	test start_all_send
	delay 5
	test show_table_4
	delay 15
#stop all send
	test stop_all_send
	test info
}

test show_table_4 {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=4
	local ovs-ofctl dump-flows edge-2 -O OpenFlow13 table=4
	local ovs-ofctl dump-flows edge-3 -O OpenFLow13 table=4
}

test delay {
	delay 30
}

test start_all_send {
	# add more virtual interfaces for host a1_100 for lbal ip-matching
	exec a1_100 ifconfig a1_100-eth0:0 100.0.0.2
	exec a1_100 ifconfig a1_100-eth0:1 100.0.0.4
	exec a1_100 ifconfig a1_100-eth0:2 100.0.0.6
	exec a1_100 iperf -c 120.0.0.1 -B 100.0.0.2 -p 80 -u -t 420 -b 16M &IPERF_A1a #---a2 -> b1 (core1)
	delay 15
	exec b1_120 iperf -c 140.0.0.2 -B 120.0.0.1 -p 80 -u -t 420 -b 18M &IPERF_B1 #---b1 -> c2 (core2)
	test delay
	exec a1_100 iperf -c 140.0.0.2 -B 100.0.0.4 -p 80 -u -t 420 -b 20M &IPERF_A2 #---a4 -> c2 (core3)  
	test delay
	# additional traffic for core 1
	exec a1_100 iperf -c 120.0.0.1 -B 100.0.0.6 -p 80 -u -t 420 -b 3M &IPERF_A1b #---a2 -> b1 (core1)
	delay 15
	exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -u -t 420 -b 22M &IPERF_A3 #---a1 -> c1 (core4)
	test delay
	test delay
	test delay
}

test stop_all_send {
	killp a1_100 IPERF_A3
	killp a1_100 IPERF_A1b
	killp a1_100 IPERF_A2
	killp b1_120 IPERF_B1
	killp a1_100 IPERF_A1a
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec b1 ip route
}

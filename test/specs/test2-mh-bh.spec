# generate network equivalent to generic test-mh
# 3 participants
# combination of inbound and outbound rules
# additional test for unmatched traffic on port 8888

mode multi-hop
participants 3
peers 1 2 3

participant 1 100 edge-1:5 08:00:27:89:3b:9f 172.0.0.1/16
participant 2 200 edge-2:5 08:00:27:92:18:1f 172.0.0.11/16
participant 3 300 edge-3:5 08:00:27:54:56:ea 172.0.0.21/16 edge-4:5 08:00:27:bd:f8:b2 172.0.0.22/16

#host AS ROUTER _ IP           # host names of form a1_100 a1_110
host h NETNUMB _ AS ROUTER

announce 1 100.0.0.0/24 110.0.0.0/24
announce 2 120.0.0.0/24 130.0.0.0/24
announce 3 140.0.0.0/24 150.0.0.0/24

flow b1 | 08:00:27:89:3b:9f

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {	
	delay 2
	test start_sender
	delay 2
	test send_traffic
	delay 10
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 insert
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 remove
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 5
	test stop_sender
}

test xfer {
	verify h1_a1 h1_c1 8888
	verify h1_b1 h1_c1 8888
	verify h1_b1 h1_c2 8888
}

test start_sender {
	exec h1_b1 iperf -s -B 120.0.0.1 -p 80 &IPERF1
}

test send_traffic {
	exec h1_a1 iperf -c 120.0.0.1 -B 100.0.0.1 -p 80 -t 25
}

test stop_sender {
	killp h1_b1 IPERF1
}

test netstat {
	exec h1_c1 netstat -ntlp
	exec h1_c2 netstat -ntlp
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec a1 ifconfig
	exec b1 ip route
	exec c1 ip route
	exec c2 ip route
	exec h1_c1 ifconfig
	exec h1_c2 ifconfig
}

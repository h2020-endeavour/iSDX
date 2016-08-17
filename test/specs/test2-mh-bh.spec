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

flow a1 80 >> c
flow b1 4321 >> c
flow b1 4322 >> c
flow c1 << 80
flow c1 << 4321
flow c2 << 4322
flow c1 | 08:00:27:89:3b:9f

listener AUTOGEN
	
test init {
	listener
}

test regress {	
	delay 2
	test netstat
	test traffic0
	delay 2
	test netstat
	test traffic1
	#test xfer
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 insert
	delay 3
	#test xfer
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 remove
	delay 3
	#test xfer
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 2
	test traffic2
	delay 2
}

test xfer {
	verify h1_a1 h1_c1 80
	verify h1_b1 h1_c1 4321
	verify h1_b1 h1_c2 4322
}

test traffic0 {
	exec h1_c1 iperf -s -B 140.0.0.1 -p 80
	exec h1_c1 iperf -s -B 140.0.0.1 -p 4321
	exec h1_c2 iperf -s -B 140.0.0.1 -p 4322

}

test traffic1 {
	exec h1_a1 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -t 5 &
	exec h1_b1 iperf -c 140.0.0.1 -B 120.0.0.1 -p 4321 -t 5 &
	exec h1_b1 iperf -c 140.0.0.1 -B 120.0.0.1 -p 4322 -t 5 &
}

test traffic2 {
	exec h1_a1 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -t 2
	exec h1_b1 iperf -c 140.0.0.1 -B 120.0.0.1 -p 4321 -t 2
	exec h1_b1 iperf -c 140.0.0.1 -B 120.0.0.1 -p 4322 -t 2
}

test netstat {
	exec h1_c1 netstat -ntlp | grep 80 | grep -v grep
	exec h1_c1 netstat -ntlp | grep 4321 | grep -v grep
	exec h1_c2 netstat -ntlp | grep 4322 | grep -v grep
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

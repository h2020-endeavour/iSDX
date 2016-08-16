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
announce 2 140.0.0.0/24 150.0.0.0/24
announce 3 140.0.0.0/24 150.0.0.0/24

flow a1 80 >> c
flow b1 4321 >> c
flow b1 4322 >> c
flow c1 << 80
flow c1 << 4321
flow c2 << 4322
flow c1 | 08:00:27:89:3b:9f

listener AUTOGEN 80 4321 4322 8888

test regress {	
	test xfer
	delay 2
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 insert
	delay 3
	test xfer
	delay 5
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 3
	blackholing 3 remove
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 2
	test info
}
	
test init {
	listener
}

test xfer {
	verify a1_100 b1_140 80
	verify a1_100 c1_140 4321
	verify a1_100 c2_140 4322
	verify a1_100 b1_140 8888
}

test info {
	local ovs-ofctl dump-flows edge-1
	exec a1 ip route
	exec b1 ip route
	exec c1 ip route
	exec c2 ip route
}

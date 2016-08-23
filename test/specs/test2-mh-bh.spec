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
flow c1 | 08:00:bb:bb:01:00

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {
	delay 60
	#start
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 5
	exec a1_100 iperf -c 120.0.0.1 -B 100.0.0.1 -p 80 -u -n 100 -t 300 -l 30 &PERF1
	delay 30
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	#insert
	blackholing 3 insert
	delay 10
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	delay 60
	#remove
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	blackholing 3 remove
	delay 10
	local ovs-ofctl dump-flows edge-1 -O Openflow13 table=2
	delay 30
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=2
	#stop
	delay 60
	test info
}

test xfer {
	verify a1_100 b1_120 8888
}

test start_sender {
	exec b1_120 iperf -s -u -B 120.0.0.1 -p 80 &IPERF1
	exec b1_120 iperf -s -u -B 120.0.0.1 -p 4323 &IPERF2
	exec b1_120 iperf -s -u -B 120.0.0.1 -p 4324 &IPERF3
}

test stop_sender {
	killp b1_120 IPERF1
	killp b1_120 IPERF2
	killp b1_120 IPERF3
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec a1 ifconfig
	exec b1 ip route
	exec b1 ipconfig
}

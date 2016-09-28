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

flow a1 80 >> b
flow a1 4321 >> c
flow a1 4322 >> c
flow c1 << 4321
flow c2 << 4322

listener AUTOGEN 80 4321 4322 8888

test regress {
    delay 5
	#test xfer
	#delay 5



    test start_all_send_80
    test delay
    test stop_all_send_80
    delay 5


    test start_all_send_4321
    test delay
    test stop_all_send_4321
    test delay


    test start_all_send_4322
    test delay
    test stop_all_send_4322
    test delay


    #test info

	withdraw b1 140.0.0.0/24
	exec a1 ip -s -s neigh flush all
	delay 2

	test start_all_send_80
    test delay
    test stop_all_send_80
    test delay

	#test xfer
	announce b1 140.0.0.0/24
	exec a1 ip -s -s neigh flush all
	delay 2
	#test xfer

	test start_all_send_80
    test delay
    test stop_all_send_80
    test delay

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



test start_all_send_80 {
    exec b1_140 iperf -s -p 80 &IPERF_P1_1
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 80 -t 40  &IPERF_P1_2
}

test stop_all_send_80 {
    killp b1_140 IPERF_P1_1
	killp a1_100 IPERF_P1_2
}

test start_all_send_4321 {
    exec c1_140 iperf -s -p 4321 &IPERF_P2_1
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 4321 -t 40  &IPERF_P2_2
}

test stop_all_send_4321 {
    killp c1_140 IPERF_P2_1
	killp a1_100 IPERF_P2_2
}

test start_all_send_4322 {
    exec c2_140 iperf -s -p 4322 &IPERF_P3_1
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 4322 -t 40  &IPERF_P3_2
}

test stop_all_send_4321 {
    killp c2_140 IPERF_P3_1
	killp a1_100 IPERF_P3_2
}


test delay {
        delay 15
}

test info {
	local ovs-ofctl -O OpenFlow13 dump-flows edge-1
	exec a1 ip route
	bgp a1
	exec b1 ip route
	bgp b1
	exec c1 ip route
	bgp c1
	exec c2 ip route
	bgp c2
}

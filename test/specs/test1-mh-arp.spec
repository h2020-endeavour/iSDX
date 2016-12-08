# generate network equivalent to generic test-mh
# 10 participants
# combination of inbound and outbound rules
# additional test for unmatched traffic on port 8888

mode multi-hop
participants 8 
peers 1 2 3 4 5 6 7 8 

participant 1 100 edge-1:5 MAC 172.0.0.1/16
participant 2 200 edge-2:5 MAC 172.0.0.11/16
participant 3 300 edge-3:5 MAC 172.0.0.21/16 edge-4:5 MAC 172.0.0.22/16
participant 4 400 edge-1:8 MAC 172.0.0.31/16
participant 5 500 edge-2:6 MAC 172.0.0.41/16
participant 6 600 edge-3:6 MAC 172.0.0.51/16
participant 7 700 edge-4:6 MAC 172.0.0.61/16
participant 8 800 edge-1:9 MAC 172.0.0.71/16

host AS ROUTER _ IP           # host names of form a1_100 a1_110

announce 1 100.0.0.0/24 110.0.0.0/24
announce 2 120.0.0.0/24 130.0.0.0/24
announce 3 140.0.0.0/24 150.0.0.0/24
announce 4 160.0.0.0/24
announce 5 170.0.0.0/24
announce 6 180.0.0.0/24
announce 7 190.0.0.0/24
announce 8 200.0.0.0/24

flow a1 80 >> b
flow a1 4321 >> c
flow a1 4322 >> c
flow c1 << 4321
flow c2 << 4322

listener AUTOGEN 80 4321 4322 8888 6666 3421

test regress {
	delay 15 
        test start_servers_iperf
        test iperf_bh
        delay 40 
        test iface_down
        test flush_route_server_arp
        delay 60 
        test iface_up
        test stop_servers_iperf
}
	
test init {
	listener
}

test iface_down {
   exec a1 ifconfig a1-eth0 down
   exec c1 ifconfig c1-eth0 down
   exec d1 ifconfig d1-eth0 down
   exec e1 ifconfig e1-eth0 down
   exec f1 ifconfig f1-eth0 down
   exec h1 ifconfig h1-eth0 down
}

test iface_up {
   exec h1 ifconfig h1-eth0 up
   exec c1 ifconfig c1-eth0 up
   exec d1 ifconfig d1-eth0 up
   exec e1 ifconfig e1-eth0 up
   exec f1 ifconfig f1-eth0 up
   exec h1 ifconfig h1-eth0 up
}

test start_servers_iperf {
    exec b1_120 iperf -s -p 80 &IPERF_SERVER1
    exec c1_140 iperf -s -p 4321 &IPERF_SERVER2
    exec a1_110 iperf -s -p 80 &IPERF_SERVER3
    exec d1_160 iperf -s -p 4322 &IPERF_SERVER4 
    exec e1_170 iperf -s -p 4321 &IPERF_SERVER5
    exec f1_180 iperf -s -p 80 &IPERF_SERVER6
    exec g1_190 iperf -s -p 6666 &IPERF_SERVER7
    exec h1_200 iperf -s -p 3421 &IPERF_SERVER8
}

test iperf_bh {
    exec b1_120 iperf -c 200.0.0.1 -p 3421 -t 60 &IPERF_BH
    delay 60
    exec a1_100 iperf -c 140.0.0.1 -p 4321 -t 10 &IPERF_AC
    exec e1_170 iperf -c 190.0.0.1 -p 6666 -t 10 &IPERF_EG
    exec f1_180 iperf -c 160.0.0.1 -p 4322 -t 10 &IPERF_FD
}

test xfer {
	verify a1_100 b1_120 80
	verify a1_100 c1_140 4321
	verify a1_100 c2_140 4322
	verify a1_100 b1_120 8888
        verify c1_140 d1_160 6666
        verify f1_180 g1_190 3421 
}

test start_all_send_3421 {
    exec a1_110 iperf -c 200.0.0.1 -p 3421 -i 30 &IPERF_1_8
    exec b1_130 iperf -c 200.0.0.1 -p 3421 -i 30 &IPERF_2_8
    exec f1_180 iperf -c 200.0.0.1 -p 3421 -t 30 &IPERF_6_8
    exec c1_140 iperf -c 200.0.0.1 -p 3421 -t 30 &IPERF_3_8
    exec e1_170 iperf -c 200.0.0.1 -p 3421 -t 30 &IPERF_5_8
}

test start_all_send_80 {
   exec a1_100 iperf -c 120.0.0.1 -p 80 -t 30 &IPERF_1_2
   exec b1_120 iperf -c 180.0.0.1 -p 80 -t 30 &IPERF_2_6
   exec d1_160 iperf -c 220.0.0.1 -p 80 -t 30 &IPERF_4_10
}

test start_all_send_4321 {
    exec c1_140 iperf -c 170.0.0.1 -p 4321 -t 30 &IPERF_3_5
    exec g1_190 iperf -c 140.0.0.1 -p 4321 -t 30 &IPERF_7_3
}

test start_all_send_8888 {
    exec e1_170 iperf -c 210.0.0.1 -p 8888 -t 30 &IPERF_5_9
    exec h1_200 iperf -c 210.0.0.1 -p 8888 -t 30 &IPERF_8_9
    exec b1_120 iperf -c 210.0.0.1 -p 8888 -t 30 &IPERF_2_9
    exec f1_180 iperf -c 210.0.0.1 -p 8888 -t 30 &IPERF_6_9
}

test start_all_send_6666 {
    exec a1_110 iperf -c 190.0.0.1 -p 6666 -t 30 &IPERF_1_8
    exec d1_160 iperf -c 190.0.0.1 -p 6666 -t 30 &IPERF_4_8
}

test flush_route_server_arp {
    local ip -s -s neigh flush all
}

test stop_servers_iperf {
   killp b1_120 IPERF_SERVER1
   killp c1_140 IPERF_SERVER2
   killp a1_110 IPERF_SERVER3
   killp d1_160 IPERF_SERVER4
   killp e1_170 IPERF_SERVER5
   killp f1_180 IPERF_SERVER6
   killp g1_190 IPERF_SERVER7
   killp h1_200 IPERF_SERVER8
}

test info {
	local ovs-ofctl -O OpenFlow13 dump-flows edge-1
        local ovs-ofctl -O OpenFlow13 dump-flows core-1
	exec a1 ip route
	bgp a1
	exec b1 ip route
	bgp b1
	exec c1 ip route
	bgp c1
	exec c2 ip route
	bgp c2
}

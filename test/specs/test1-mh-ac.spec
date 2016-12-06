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

announce 1 100.0.0.0/24
announce 2 140.0.0.0/24
announce 3 150.0.0.0/24

flow a1 179 >> c

listener AUTOGEN 80 179

test regress {
    delay 5

    test info
    exec a1 ip route
    exec a1 ping -c 1 140.0.0.1
    exec a1 ping -c 1 150.0.0.1
    exec a1 arp
    delay 40
    exec a1 python /home/vagrant/iSDX/test/generate_bgp_packet.py 40 a1-eth0 0.1
    delay 30
    exec a1 python /home/vagrant/iSDX/test/generate_ospf_packet.py 40 a1-eth0 0.1
    delay 2
    #local ovs-ofctl add-flow edge-1 table=0,eth_type=0x800,ip_proto=17,actions=output:1
    test info




    delay 20

}

test init {
   listener
}

test xfer {
   verify a1_100 b1_140 80
   verify a1_100 c1_150 179
}


test delay {
        delay 40
}

test info {
   local ovs-ofctl -O OpenFlow13 dump-flows edge-1
   #exec a1 ip route
   #bgp a1
   #exec b1 ip route
   #bgp b1
   #exec c1 ip route
   #bgp c1
   #exec c2 ip route
   #bgp c2
}
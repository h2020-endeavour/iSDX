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
announce 3 140.0.0.0/24

flow a1 80 >> b
flow a1 4321 >> c
flow a1 4322 >> c
flow c1 << 4321
flow c2 << 4322
flow c1 1 | a1 ipv4_dst=140.0.0.1 udp_dst=53

listener AUTOGEN 80 4321 4322 8888

test regress {
 blackholing 3 insert 1
 test info
}

test init {
   #listener
}


test delay {
        delay 40
}

test info {
   local ovs-ofctl -O OpenFlow13 dump-flows edge-1
   }
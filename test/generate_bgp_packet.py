from scapy.all import *
import sys
import time

iterations=float(sys.argv[1])/float(sys.argv[3])

for i in range(0,int(iterations)):
    sendp(Ether()/IP(proto=6,src="172.0.0.1",dst="150.0.0.1")/TCP(dport=179),iface=sys.argv[2])
    time.sleep(float(sys.argv[3]))
from scapy.all import *
import time
import sys

iterations=float(sys.argv[1])/float(sys.argv[3])

load_contrib('ospf')
for i in range(0,int(iterations)):
    sendp(Ether()/IP(proto=89)/OSPFv3_Type_7_LSA(),iface=sys.argv[2])
    time.sleep(float(sys.argv[3]))
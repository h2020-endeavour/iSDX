#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)

import argparse
import atexit
import json
import os
from multiprocessing.connection import Client
from signal import signal, SIGTERM
from sys import exit
from threading import Thread

''' client for participants to send policy updates '''
class BGPFlowSClient(object):
    
    def __init__(self, id):
        # participant id
        self.id = id
        self.port = str('505')+str(id)
        # used to signal termination
        self.run = True
        

    def process_handler(self, action, id_list):        
        print int(self.port)
        # Connect to bgp_flow_server
        self.client = Client(('127.0.0.1', int(self.port)))

        neighbour = 'neighbor 172.0.0.21'
        data = action + ' flow route'

        command = neighbour + ' ' + data  + ' ' + id_list 
        print command

        #announcement = neighbour 172.0.0.21 announce flow route 
        #"withdraw flow route {\\n match {\\n source 10.0.0.1/32;\\n destination 1.2.3.4/32;\\n }\\n then {\\n discard;\\n }\\n }\\n\n

        # Send data
        print "BGPFlowClient(%s): send: %s" % (self.id, command)
        self.client.send(command)

    def stop(self):
        # Stop participant client
        print "BGPFlowClient(%s): close connection" % self.id
        self.run = False
    

''' participant client useage: participant_client.py policy_file participant_id insert/remove '''
def main():
    # Set valid actions
    valid_actions = {"announce", "withdraw"}

    # Parse arugments
    parser = argparse.ArgumentParser()
    parser.add_argument('id', type=int, help='participant id (integer)')
    parser.add_argument('action', type=str, choices=valid_actions, help='use announce or withdraw')
    parser.add_argument('id_list', type=str, nargs='?', help='list of commands')
    args = parser.parse_args()

    # logger
    print "Starting BGPFlowClient(%s) with config file" % (args.id)

    # start bgp_flow_client
    bgpfclnt = BGPFlowSClient(args.id)
    bgpfclnt_thread = Thread(target=bgpfclnt.process_handler(args.action, args.id_list))
    bgpfclnt_thread.daemon = True
    bgpfclnt_thread.start()

    atexit.register(bgpfclnt.stop)
    signal(SIGTERM, lambda signum, stack_frame: exit(1))

    while bgpfclnt_thread.is_alive():
        try:
            bgpfclnt_thread.join(1)
        except KeyboardInterrupt:
            bgpfclnt.stop()

    print "BGPFlowClient(%s): extiting" % args.id
    print "done"


if __name__ == '__main__':
    main()
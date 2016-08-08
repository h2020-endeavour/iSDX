#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)

import argparse
import atexit
import json
from multiprocessing.connection import Listener, Client
import os
from signal import signal, SIGTERM
from sys import exit
from threading import RLock, Thread
from lib import PConfig


class XRS_Client(object):
    def __init__(self, id, config_file):
        # participant id
        self.id = id

        # used to signal termination
        self.run = True
        self.prefix_lock = {}

        # Initialize participant params
        self.cfg = PConfig(config_file, self.id)

def xstart(self, test_file):
        # Start all clients/listeners/whatevs
        print("Starting XRS_Client for participant %s" % self.id)


        # Route server client, Reference monitor client, Arp Proxy client
        self.xrs_client = self.cfg.get_xrs_client()
        self.xrs_client.send(test_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('test_file', help='the test file')
    parser.add_argument('id', type=int,
                   help='participant id (integer)')
    args = parser.parse_args()

    # locate test file
    # TODO: Separate the config files for each participant
    base_path = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                ".."))
    test_file = os.path.join(base_path, args.test_file)

    # locate config file
    # TODO: Separate the config files for each participant
    base_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                "..","examples","test-mh","config"))
    config_file = os.path.join(base_path, "sdx_global.cfg")

    #logger = util.log.getLogger("P_" + str(args.id))

    print ("Starting controller with config file: "+str(config_file))

    # start controller
    xrsctrlr = XRS_Client(args.id, config_file)
    xrsctrlr_thread = Thread(target=xrsctrlr.xstart(test_file))
    xrsctrlr_thread.daemon = True
    xrsctrlr_thread.start()

    atexit.register(xrsctrlr.stop)
    signal(SIGTERM, lambda signum, stack_frame: exit(1))

    while xrsctrlr_thread.is_alive():
        try:
            xrsctrlr_thread.join(1)
        except KeyboardInterrupt:
            xrsctrlr.stop()

    print ("Xrsctrlr exiting")


if __name__ == '__main__':
    main()
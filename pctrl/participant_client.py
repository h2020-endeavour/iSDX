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
import util.log

''' client for participants to send policy updates '''
class ParticipantClient(object):
    
    def __init__(self, id, config_file, logger):
        # participant id
        self.id = id

        # used to signal termination
        self.run = True
        #self.prefix_lock = {}

        # Initialize participant params and logger
        self.cfg = PConfig(config_file, self.id)
        self.logger = logger

    def xstart(self, policy_file, action):

        validate_actions = {"remove", "insert"}
        if action in validate_actions:
            self.logger.debug("found %s in validate_actions" % action)

        # Initalize participant client
        self.logger.debug("participant_client(%s): start client" % self.id)
        self.client = self.cfg.get_participant_client(self.id, self.logger)
        
        # Open File and Send
        with open(policy_file, 'r') as f:
            raw_data = json.load(f)
            data = '{ "policy": [ { "%s": [ %s ] } ] }' % (action, raw_data)

        self.logger.debug("participant_client(%s): send: %s" % (self.id, data))
        self.client.send(data)


    def stop(self):
        
        # Stop participant client
        self.logger.debug("participant_client(%s): close connection"  % self.id)
        self.run = False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('policy_file', help='the policy change file')
    parser.add_argument('id', type=int,
                   help='participant id (integer)')
    parser.add_argument('action', help='use remove or insert')
    args = parser.parse_args()

    # locate policy changefile
    # TODO: atm same path as this program
    base_path = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                ".."))
    policy_change_file = os.path.join(base_path, args.policy_file)

    # locate config file
    # TODO: hard coded destination to global config file
    base_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                "..","..","endeavour","examples","test-mh","config"))
    config_file = os.path.join(base_path, "sdx_global.cfg")

    logger = util.log.getLogger("P_" + str(args.id))
    logger.debug ("Starting participant_client with config file: "+str(config_file))

    # start controller
    prtclnt = ParticipantClient(args.id, config_file, logger)
    prtclnt_thread = Thread(target=prtclnt.xstart(policy_change_file, args.action))
    prtclnt_thread.daemon = True
    prtclnt_thread.start()

    atexit.register(prtclnt.stop)
    signal(SIGTERM, lambda signum, stack_frame: exit(1))

    while prtclnt_thread.is_alive():
        try:
            prtclnt_thread.join(1)
        except KeyboardInterrupt:
            prtclnt.stop()

    logger.debug ("participant_client extiting")
    print ("done")


if __name__ == '__main__':
    main()
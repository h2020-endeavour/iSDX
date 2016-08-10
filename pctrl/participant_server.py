#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)


import json
from multiprocessing.connection import Listener
from threading import Thread

import os
import sys
np = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if np not in sys.path:
    sys.path.append(np)
import util.log


''' Server of Reference Monitor to Receive Flow Mods '''
class ParticipantServer(object):

    def __init__(self, participant_controller, address, port, logger):
        self.logger = logger
        self.logger.info('participant_server: start')

        self.controller = participant_controller
        #self.listener = Listener((address, port), authkey=str(key), backlog=100)
        self.listener = Listener((address, port), backlog=100)

    def start(self):
        self.receive = True
        self.receiver = Thread(target=self.receiver)
        self.receiver.start()

    ''' receiver '''
    def receiver(self):
        while self.receive:
            conn = self.listener.accept()
            self.logger.info('participant_server: accepted connection from ' + str(self.listener.last_accepted))

            msg = None
            while msg is None:
                try:
                    msg = conn.recv()
                except:
                    pass
            self.logger.info('participant_server: received message')
            self.controller.process_event(json.loads(msg))

            conn.close()
            self.logger.info('server: closed connection')

    def stop(self):
        self.receive = False
        self.receiver.join(1)

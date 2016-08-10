#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)

import json
from multiprocessing.connection import Listener
from threading import Thread

import os
import sys

''' Server for Participants to handle Policy Updates '''
class ParticipantServer(object):

    def __init__(self, participant_controller, address, port, logger):
        self.logger = logger
        self.logger.info('participant_server(%s): start server' % participant_controller.id)

        self.controller = participant_controller
        self.listener = Listener((address, port), backlog=100)

    def start(self):
        self.receive = True
        self.receiver = Thread(target=self.receiver)
        self.receiver.start()

    def receiver(self):
        while self.receive:
            conn = self.listener.accept()
            self.logger.info('participant_server(%s) accepted connection from %s' % (participant_controller.id, self.listener.last_accepted))

            msg = None
            while msg is None:
                try:
                    msg = conn.recv()
                except:
                    pass
            self.logger.debug('participant_server(%s): received message' % participant_controller.id)
            self.controller.process_event(json.loads(msg))

            conn.close()
            self.logger.debug('participant_server(%s): closed connection' % participant_controller.id)

    def stop(self):
        self.receive = False
        self.receiver.join(1)

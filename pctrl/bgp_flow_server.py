#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)


''' server for bgp flow sequence '''
import json
from multiprocessing.connection import Listener
from threading import Thread

class BGPFlowServer(object):

    def __init__(self, address, port, logger):
        
        if address == 'localhost' or address == '127.0.0.1':
            address = '127.0.0.1'
        self.address = address
        self.port = port
        self.logger = logger
        print 'server: %s port: %s' % (address, port)
        self.listener = Listener((self.address, int(self.port)), backlog=100)

    def start(self, participant_controller):
        self.receive = True
        self.controller = participant_controller
        self.id = self.controller.id
        self.logger.debug('bgp_flow_server(%s): start server on %s:%s' % (self.id, self.address, self.port))

        self.receiver = Thread(target=self.receiver)
        self.receiver.start()

    def receiver(self):
        while self.receive:
            conn = self.listener.accept()
            self.logger.debug('bgp_flow_server(%s) accepted connection from %s' % (self.id, self.listener.last_accepted))

            msg = None
            while msg is None:
                try:
                    msg = conn.recv()
                except:
                    pass
            self.logger.debug('bgp_flow_server(%s): received message: %s' % (self.id, msg))
            #self.controller.process_event(json.loads(msg))
            self.controller.send_announcement(msg)

            conn.close()
            self.logger.debug('bgp_flow_server(%s): closed connection' % self.id)

    def stop(self):
        self.receive = False
        self.receiver.join(1)
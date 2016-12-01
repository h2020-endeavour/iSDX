#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)


''' server for participants api to handle policy updates '''
import BaseHTTPServer
from participant_api_handler import ApiHandler
from threading import Thread

class ParticipantAPI(object):

    def __init__(self, address, port, logger):
        
        #if address == 'localhost' or address == '127.0.0.1':
        #    address = '127.0.0.1'
        self.address = address
        self.port = port
        self.logger = logger  

    def start(self, participant_controller):

        ApiHandler.controller = participant_controller
    
        self.controller = participant_controller
        self.id = self.controller.id
        self.logger.error('part: %s address: %s port: %s' % (self.id, self.address, self.port))
        

        server_class = BaseHTTPServer.HTTPServer
        self.httpd = server_class((str(self.address), int(self.port)), ApiHandler)

        self.api = Thread(target=self.api)
        self.api.start()

    def api(self):
        try:
            self.logger.debug('participant_api(%s): start server' % self.id)
            self.httpd.serve_forever()
        except:
            self.logger.debug('participant_api(%s): closed connection due exception' % self.id)
        

    def stop(self):
        self.logger.debug('participant_api(%s): closed connection due stop' % self.id)
        self.httpd.server_close()
        self.api.join(1)

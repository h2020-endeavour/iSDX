#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)


''' server for participants api to handle policy updates '''
import BaseHTTPServer
from participant_api_handler import ApiHandler

class ParticipantAPI(object):

    def __init__(self, address, port, logger, participant_controller):
        self.logger = logger
        self.controller = participant_controller
        ApiHandler.controller = self.controller
        self.id = self.controller.id
        
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((address, port), ApiHandler)
        try:
            self.logger.debug('participant_api(%s): start server' % self.id)
            httpd.serve_forever()
        except:
            pass
        self.logger.debug('participant_api(%s): closed connection' % self.id)
        httpd.server_close()

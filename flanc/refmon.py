#  Author:
#  Rudiger Birkner (Networked Systems Group ETH Zurich)


import json
from multiprocessing import Queue
import os
from Queue import Empty
from time import time

from ryu import cfg
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_0, ofproto_v1_3

import sys
np = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if np not in sys.path:
    sys.path.append(np)
import util.log

from lib import MultiSwitchController, MultiTableController, MultiHopController, Config, InvalidConfigError
from ofp10 import FlowMod as OFP10FlowMod
from ofp13 import FlowMod as OFP13FlowMod
from server import Server
from rest import AnomalyDetectionReceiver
from ryu.app.wsgi import WSGIApplication
LOG = True

class RefMon(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION, ofproto_v1_3.OFP_VERSION]
    _CONTEXTS = { 'wsgi': WSGIApplication }

    def __init__(self, *args, **kwargs):
        super(RefMon, self).__init__(*args, **kwargs)

        # Use REST API for Anomaly Detection for now
        wsgi = kwargs['wsgi']
        wsgi.register(AnomalyDetectionReceiver, self)

        self.logger = util.log.getLogger('ReferenceMonitor')
        self.logger.info('refmon: start')

        # retrieve command line arguments
        CONF = cfg.CONF

        log_file_path = CONF['refmon']['log']
        if log_file_path is not None:
            log_file = os.path.abspath(log_file_path)
            self.log = open(log_file, "w")
        else:
            self.log = None

        # configure flow mod logging
        log_file_path = CONF['refmon']['flowmodlog']
        if log_file_path is not None:
            log_file = os.path.abspath(log_file_path)
            self.flow_mod_log = open(log_file, "w")
        else:
            self.flow_mod_log = None

        # load config from file
        self.logger.info('refmon: load config')
        try:
            config_file_path = CONF['refmon']['config']
            config_file = os.path.abspath(config_file_path)
            self.config = Config(config_file)
        except InvalidConfigError as e:
            self.logger.info('refmon: invalid config '+str(e))
            # No sense to continue the execution             
            sys.exit()            

        self.config.always_ready = CONF['refmon']['always_ready']

        # start controller
        if self.config.isMultiSwitchMode():
            self.controller = MultiSwitchController(self.config)
        elif self.config.isMultiTableMode():
            self.controller = MultiTableController(self.config)
        elif self.config.isMultiHopMode():
			self.controller = MultiHopController(self.config)

	# this must be set before Server, which uses it.
        self.flow_mod_times = Queue()

        # start server receiving flowmod requests
        self.server = Server(self, self.config.server["IP"], self.config.server["Port"], self.config.server["key"])
        self.server.start()

    def close(self):
        self.logger.info('refmon: stop')

        if self.log:
            self.log.close()
        if self.flow_mod_log:
            self.flow_mod_log.close()

        self.server.stop()

    @set_ev_cls(ofp_event.EventOFPStateChange, [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def dp_state_change_handler(self, ev):
        datapath = ev.datapath

        if ev.state == MAIN_DISPATCHER:
            self.controller.switch_connect(datapath)
        elif ev.state == DEAD_DISPATCHER:
            self.controller.switch_disconnect(datapath)
        
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        self.controller.packet_in(ev)

    @set_ev_cls(ofp_event.EventOFPBarrierReply, MAIN_DISPATCHER)
    def barrier_reply_handler(self, ev):
        datapath = ev.msg.datapath
        if self.controller.handle_barrier_reply(datapath):
            end_time = time()

            try:
                start_time = self.flow_mod_times.get_nowait()
            except Empty:
                pass

            if self.log:
                self.log.write(str(start_time) + " " + str(end_time) + " " + str(end_time - start_time) + "\n")

    def process_flow_mods(self, msg):
        self.flow_mod_times.put(time())

        self.logger.info('refmon: received flowmod request')

        # authorization
        if "auth_info" in msg:
            auth_info = msg["auth_info"]

            # TODO: FLANC authorization here
           
            origin = auth_info["participant"]

            if "flow_mods" in msg:

                flow_mods = msg["flow_mods"]
                # Flows from the participant come without the switch
                # The fabric controllers picks the switches where
                # they shall be installed
               
                participant = str(msg['auth_info']['participant']) 
                if participant in self.config.participants:                    
                    flow_mods = self.controller.distribute_participant_flows(flow_mods, self.config.participants[participant])

                 # flow mod logging
                if self.flow_mod_log:
                    self.flow_mod_log.write('BURST: ' + str(time()) + '\n')
                    self.flow_mod_log.write('PARTICIPANT: ' + str(msg['auth_info']['participant']) + '\n')
                    for flow_mod in flow_mods:
                        self.flow_mod_log.write(json.dumps(flow_mod) + '\n')
                    self.flow_mod_log.write('\n')

                self.logger.debug('BURST: ' + str(time()))
                self.logger.debug('PARTICIPANT: ' + str(msg['auth_info']['participant']))
                for flow_mod in flow_mods:
                    self.logger.debug('FLOWMOD from ' + str(origin) + ': ' + json.dumps(flow_mod))
                # push flow mods to the data plane
                for flow_mod in flow_mods:
                    if self.config.ofv == "1.0":
                        fm = OFP10FlowMod(self.config, origin, flow_mod)
                    elif self.config.ofv == "1.3":
                        fm = OFP13FlowMod(self.config, origin, flow_mod)
                    self.logger.debug("rule validated. match: " + str(fm.matches) + " table:" + str(fm.table) + " cookie:" + str(fm.cookie))
                    self.controller.process_flow_mod(fm)

    @set_ev_cls(ofp_event.EventOFPErrorMsg, MAIN_DISPATCHER)
    def error_msg_handler(self, ev):
        msg = ev.msg

        print 'error msg type 0x%x code 0x%x' % (msg.type, msg.code)

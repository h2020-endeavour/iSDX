#  Author:
#  Rudiger Birkner (Networked Systems Group ETH Zurich)

import abc
import json
import logging
import copy

from Queue import Queue

import os
import sys
np = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if np not in sys.path:
    sys.path.append(np)
import util.log


from ofdpa20 import OFDPA20

IP_ETH_TYPE = 0x0800
ARP_ETH_TYPE = 0x0806
TCP_IP_PROTO = 6

# PRIORITIES
FLOW_MISS_PRIORITY = 0
BGP = 179
BGP_PRIORITY = 8
ARP_PRIORITY = 7
# COOKIES
NO_COOKIE = 0

class Config(object):

    MULTISWITCH = 0
    MULTITABLE  = 1
    MULTIHOP = 2

    def __init__(self, config_file):
        self.server = None
        # Controller mode name
        self.mode_name = None
        # Controller mode alias
        self.mode_alias = None
        self.mode = None
        self.ofdpa = set()
        self.ofv = None
        self.tables = None
        self.dpids = None
        self.dp_alias = []
        self.dpid_2_name = {}
        self.datapath_ports = None

        self.datapaths = {}
        self.parser = None
        self.ofproto = None
        self.participants = {}

        # loading config file
        config = json.load(open(config_file, 'r'))

        # read from file
        if "Mode" in config:
            mode = config["Mode"]
            # Create an alias from the first letter of each word of the config mode 
            alias_prefix = "".join( [mode.split('-')[0][0], mode.split('-')[1][0]] )
            self.mode_alias = "%s_ctrlr" % (alias_prefix.lower())
            self.name =  "".join(mode.split('-'))
            if mode == "Multi-Switch":
                self.mode = self.MULTISWITCH
            elif mode == "Multi-Table":
                self.mode = self.MULTITABLE
            elif mode == "Multi-Hop": 
                self.mode = self.MULTIHOP
        if "RefMon Settings" in config:
            if "fabric options" in config["RefMon Settings"]:
                if "tables" in config["RefMon Settings"]["fabric options"]:
                    self.tables = config["RefMon Settings"]["fabric options"]["tables"]
                if "dpids" in config["RefMon Settings"]["fabric options"]:
                    self.dpids = config["RefMon Settings"]["fabric options"]["dpids"]
                    for k,v in self.dpids.iteritems():
                        self.dpid_2_name[v] = k
                if "dp alias" in config["RefMon Settings"]["fabric options"]:
                    self.dp_alias = config["RefMon Settings"]["fabric options"]["dp alias"]
                if "OF version" in config["RefMon Settings"]["fabric options"]:
                    self.ofv = config["RefMon Settings"]["fabric options"]["OF version"]
                if "ofdpa" in config["RefMon Settings"]["fabric options"]:
                    self.ofdpa = set(config["RefMon Settings"]["fabric options"]["ofdpa"])

            if "fabric connections" in config["RefMon Settings"]:
                self.datapath_ports = config["RefMon Settings"]["fabric connections"]

        if "RefMon Server" in config:
            self.server = config["RefMon Server"]
        else:
            raise InvalidConfigError(config)

        if "Participants" in config:
            self.participants = config["Participants"]

        # check if valid config
        if self.isMultiSwitchMode():
            if not (self.ofv and self.dpids and self.datapath_ports):
                raise InvalidConfigError(config)
        elif self.isMultiTableMode():
            if not (self.ofv == "1.3" and self.tables and self.datapath_ports):
                raise InvalidConfigError(config)
        elif self.isMultiHopMode():
            #TODO: Implement check for edges and nodes
            if (not self.checkMultiHopConfig()):
		        raise InvalidConfigError(config)    
        else:
            raise InvalidConfigError(config)

    def isMultiSwitchMode(self):
        return self.mode == self.MULTISWITCH

    def isMultiTableMode(self):
        return self.mode == self.MULTITABLE

    def isMultiHopMode(self):
        return self.mode == self.MULTIHOP

    def checkMultiHopConfig(self):
        # For now check if there is at least one edge switch
        # It is does not ensure the file is correct, but a
        # weak enforcement         
        for switch in self.dpids:
            if switch.find("edge") >= 0:
                return True
        return False

class InvalidConfigError(Exception):
    def __init__(self, config):
        self.config = config
    def __str__(self):
        return repr(self.config)

# Base class for iSDX reference monitor controllers

class Controller(object):
    __metaclass__ = abc.ABCMeta    
    def __init__(self, config):
        self.config = config
        self.fm_queue = Queue()        
        self.logger = util.log.getLogger("%sController" %(config.name))
              
    def switch_connect(self, dp):
   
        dp_name = self.config.dpid_2_name[dp.id]
        self.config.datapaths[dp_name] = dp

        if self.config.ofproto is None:
            self.config.ofproto = dp.ofproto
        if self.config.parser is None:
            self.config.parser = dp.ofproto_parser

        self.logger.info('%s: switch connect: %s' % (self.config.mode_alias, dp_name))

        if self.is_ready():
            self.init_fabric()

            while not self.fm_queue.empty():
                self.process_flow_mod(self.fm_queue.get())

    def is_ready(self):
        if len(self.config.datapaths) == len(self.config.dpids) or self.config.always_ready:
            return True
        return False
    
    def switch_disconnect(self, dp):
        if dp.id in self.config.dpid_2_name:
            dp_name = self.config.dpid_2_name[dp.id]
            self.logger.info('%s: switch disconnect: %s' % (self.config.mode_alias, dp_name))
            del self.config.datapaths[dp_name]

    def packet_in(self, ev):
        self.logger.info("%s: packet in" % (self.config.mode_alias))
    

    def distribute_participant_flows(self, flow_mods, participant):
        # TODO: Make it better, too ugly right now :(
        new_flows = []
        for flow in flow_mods:
            rule_type = flow["rule_type"]
            # Install only in the participant edges            
            if rule_type == "outbound":
                for port in participant["Ports"]:
                    datapath = port["switch"]
                    if datapath.find("edge") == 0:
                        # Delete old flow and add new one
                        new_flow = copy.deepcopy(flow) 
                        new_flow["datapath"] = datapath
                        new_flows.append(new_flow)
            # Install in all edges        
            elif rule_type == "inbound":
                edges = [x for x in self.config.dpids if x.find("edge") == 0]
                for e in edges:
                    new_flow = copy.deepcopy(flow) 
                    #print new_flow
                    new_flow["datapath"] = e
                    new_flows.append(new_flow)        
        if len(new_flows) > 0:
            return new_flows
        return flow_mods

    @abc.abstractmethod
    def init_fabric(self):
        pass

    @abc.abstractmethod
    def process_flow_mod(self, fm):
        pass
    
    @abc.abstractmethod
    def send_barrier_request(self):
        pass

    @abc.abstractmethod
    def handle_barrier_reply(self):
        pass

class MultiTableController(Controller):
    def __init__(self, config):
        super(MultiTableController, self).__init__(config)
        self.logger.info('%s: creating an instance of MultiTableController' % (self.config.mode_alias))

    def init_fabric(self):
        # install table-miss flow entry
        match = self.config.parser.OFPMatch()
        actions = [self.config.parser.OFPActionOutput(self.config.ofproto.OFPP_CONTROLLER, self.config.ofproto.OFPCML_NO_BUFFER)]
        instructions = [self.config.parser.OFPInstructionActions(self.config.ofproto.OFPIT_APPLY_ACTIONS, actions)]

        for table in self.config.tables.values():
            mod = self.config.parser.OFPFlowMod(datapath=self.config.datapaths["main"],
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority=FLOW_MISS_PRIORITY,
                                                match=match, instructions=instructions)
            self.config.datapaths["main"].send_msg(mod)

        mod = self.config.parser.OFPFlowMod(datapath=self.config.datapaths["arp"],
                                            cookie=NO_COOKIE, cookie_mask=1,
                                            command=self.config.ofproto.OFPFC_ADD,
                                            priority=FLOW_MISS_PRIORITY,
                                            match=match, instructions=instructions)
        self.config.datapaths["arp"].send_msg(mod)

    def process_flow_mod(self, fm):
        if not self.is_ready():
            self.fm_queue.put(fm)
        else:
            mod = fm.get_flow_mod(self.config)
            self.config.datapaths[fm.get_dst_dp()].send_msg(mod)

    def send_barrier_request(self):
        request = self.config.parser.OFPBarrierRequest(self.config.datapaths["main"])
        self.config.datapaths["main"].send_msg(request)

    def handle_barrier_reply(self, datapath):
        if self.config.datapaths["main"] == datapath:
            return True
        return False

class MultiSwitchController(Controller):
    def __init__(self, config):
        super(MultiSwitchController, self).__init__(config)
        self.logger.info('%s: creating an instance of MultiSwitchController' % (self.config.mode_alias))
        self.config = config
        self.last_command_type = {}

    def init_fabric(self):
        # install table-miss flow entry
        self.logger.info('%s: init fabric' % (self.config.mode_alias))
        match = self.config.parser.OFPMatch()

        if self.config.ofv  == "1.3":
            actions = [self.config.parser.OFPActionOutput(self.config.ofproto.OFPP_CONTROLLER, self.config.ofproto.OFPCML_NO_BUFFER)]
            instructions = [self.config.parser.OFPInstructionActions(self.config.ofproto.OFPIT_APPLY_ACTIONS, actions)]
        else:
            actions = [self.config.parser.OFPActionOutput(self.config.ofproto.OFPP_CONTROLLER)]

        for datapath in self.config.datapaths.values():
            if self.config.ofv  == "1.3":
                mod = self.config.parser.OFPFlowMod(datapath=datapath,
                                                    cookie=NO_COOKIE, cookie_mask=3,
                                                    command=self.config.ofproto.OFPFC_ADD,
                                                    priority=FLOW_MISS_PRIORITY,
                                                    match=match, instructions=instructions)
            else:
                mod = self.config.parser.OFPFlowMod(datapath=datapath,
                                                    cookie=NO_COOKIE,
                                                    command=self.config.ofproto.OFPFC_ADD,
                                                    priority=FLOW_MISS_PRIORITY,
                                                    match=match, actions=actions)
            datapath.send_msg(mod)

    def process_flow_mod(self, fm):
        if not self.is_ready():
            self.fm_queue.put(fm)
        else:
            dp = self.config.datapaths[fm.get_dst_dp()]
            if self.config.dpid_2_name[dp.id] in self.config.ofdpa:
                ofdpa = OFDPA20(self.config)
                flow_mod, group_mods = fm.get_flow_and_group_mods(self.config)
                for gm in group_mods:
                    if not ofdpa.is_group_mod_installed_in_switch(dp, gm):
                        dp.send_msg(gm)
                        ofdpa.mark_group_mod_as_installed(dp, gm)
            else:
                flow_mod = fm.get_flow_mod(self.config)
            if (not dp.id in self.last_command_type or (self.last_command_type[dp.id] != flow_mod.command)):
                self.logger.info('refmon: sending barrier')
                self.last_command_type[dp.id] = flow_mod.command
                dp.send_msg(self.config.parser.OFPBarrierRequest(dp))
            dp.send_msg(flow_mod)

    def send_barrier_request(self):
        if self.is_ready():
            dp = self.config.datapaths["outbound"]
            request = self.config.parser.OFPBarrierRequest(dp)
            dp.send_msg(request)
            return True
        else:
            return False

    def handle_barrier_reply(self, datapath):
        if self.config.datapaths["outbound"] == datapath:
            return True
        return False

class MultiHopController(Controller):
    def __init__(self, config):
        super(MultiHopController, self).__init__(config)
        self.logger.info('%s: creating an instance of MultiHopController' % (self.config.mode_alias))

    def process_flow_mod(self, fm):
        if not self.is_ready():
            self.fm_queue.put(fm)
        else:
            mod = fm.get_flow_mod(self.config)
            self.config.datapaths[fm.get_dst_dp()].send_msg(mod)

    def install_default_flow(self, datapath, table_id):
        match = self.config.parser.OFPMatch()
        actions = [self.config.parser.OFPActionOutput(self.config.ofproto.OFPP_CONTROLLER, self.config.ofproto.OFPCML_NO_BUFFER)]
        instructions = [self.config.parser.OFPInstructionActions(self.config.ofproto.OFPIT_APPLY_ACTIONS, actions)]
        mod = self.config.parser.OFPFlowMod(datapath=datapath,
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table_id,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority=FLOW_MISS_PRIORITY,
                                                match=match, instructions=instructions)
        datapath.send_msg(mod)

    def default_monitoring(self, datapath, table_id, goto_table):
        match = self.config.parser.OFPMatch()
        instructions = [self.config.parser.OFPInstructionGotoTable(goto_table)]
        mod = self.config.parser.OFPFlowMod(datapath=datapath,
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table_id,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority=FLOW_MISS_PRIORITY,
                                                match=match, instructions=instructions)
        datapath.send_msg(mod)

    def default_access_control(self, datapath, table_id, goto_table):
        match = self.config.parser.OFPMatch()
        instructions = [self.config.parser.OFPInstructionGotoTable(goto_table)]
        mod = self.config.parser.OFPFlowMod(datapath=datapath,
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table_id,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority=FLOW_MISS_PRIORITY,
                                                match=match, instructions=instructions)
        datapath.send_msg(mod)


    # Create flow to send every BGP packet to the umbrella table
    def handle_BGP(self, edge, table, goto_table):
        match = self.config.parser.OFPMatch(eth_type=IP_ETH_TYPE, ip_proto = TCP_IP_PROTO, tcp_src = BGP)
        instructions = [self.config.parser.OFPInstructionGotoTable(goto_table)]        
        mod = self.config.parser.OFPFlowMod(datapath=edge,
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority = BGP_PRIORITY,
                                                match=match, instructions=instructions)
        edge.send_msg(mod)
    
    def handle_ARP(self, edge, table, goto_table):
        match = self.config.parser.OFPMatch(eth_type=ARP_ETH_TYPE)
        instructions = [self.config.parser.OFPInstructionGotoTable(goto_table)]        
        mod = self.config.parser.OFPFlowMod(datapath=edge,
                                                cookie=NO_COOKIE, cookie_mask=1,
                                                table_id=table,
                                                command=self.config.ofproto.OFPFC_ADD,
                                                priority = ARP_PRIORITY,
                                                match=match, instructions=instructions)
        edge.send_msg(mod)    

    def init_fabric(self):
        monitor = False
        tables = self.config.tables
        umbrella_core_table = tables["umbrella-core"]
        umbrella_edge_table = tables["umbrella-edge"]
        access_control_table = tables["access-control"]
        lb_table = tables["load-balancer"]
        iSDX_tables = {x:tables[x] for x in tables if x.find("umbrella") < 0}
        if "monitor" in iSDX_tables:
            monitor = True
        if "access-control" in iSDX_tables:
            access_control = True
        # Need to init more tables in the edges
        datapaths = self.config.datapaths
        edges = [datapaths[x] for x in datapaths if x.find("edge") == 0]
        for edge in edges:
            # iSDX tables            
            for table in iSDX_tables:
                if table != "monitor" and table != "access-control":
                    table_id = iSDX_tables[table]
                    self.install_default_flow(edge, table_id)
            # TODO: Send these packets to the load-balancer table?
            self.install_default_flow(edge, umbrella_edge_table)
            if access_control:
                self.default_access_control(edge, iSDX_tables["access-control"], iSDX_tables["load-balancer"])
            if monitor:
                self.default_monitoring(edge, iSDX_tables["monitor"], iSDX_tables["main-in"])
            #self.handle_BGP(edge, iSDX_tables["main-in"], lb_table)
            #self.handle_ARP(edge, iSDX_tables["main-in"], umbrella_edge_table)
            self.handle_BGP(edge, iSDX_tables["main-in"], access_control_table)
            self.handle_ARP(edge, iSDX_tables["main-in"], access_control_table)
        # Only one table for the cores
        cores = [datapaths[x] for x in datapaths if x.find("core") == 0]
        for core in cores:
            if monitor:
                self.default_monitoring(core, iSDX_tables["monitor"], iSDX_tables["main-in"])
            self.install_default_flow(core, umbrella_core_table)            

    def send_barrier_request(self):
        pass  

    def handle_barrier_reply(self, datapath):
        pass

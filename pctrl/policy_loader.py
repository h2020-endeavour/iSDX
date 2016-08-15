import os
import json
from ss_rule_scheme import update_outbound_rules, init_inbound_rules, init_outbound_rules, msg_clear_all_outbound, ss_process_policy_change


base_path = os.path.abspath(os.path.join(os.path.realpath(__file__),
                                ".."))

test_file = os.path.join(base_path, "blackholing_test.py")
with open(test_file, 'r') as f:
	data = json.load(f)

inbound_policies = []
outbound_policies = []

for element in data['policy']:
    if 'inbound' in element:
        inbound_policies = element
    if 'outbound' in element:
        outbound_policies = element

#print inbound_policies

final_switch = "main-in"
rule_msgs = init_inbound_rules(1, inbound_policies,[],final_switch)
print "Rule Messages to be removed INBOUND:: "+str(rule_msgs)


#rule_msgs2 = init_outbound_rules(1, outbound_policies, [], final_switch)
#print ("Rule Messages OUTBOUND:: "+str(rule_msgs2))

#if 'changes' in rule_msgs2:
#    if 'changes' not in rule_msgs:
#        rule_msgs['changes'] = []
#    rule_msgs['changes'] += rule_msgs2['changes']

        #TODO: Initialize Outbound Policies from RIB
print ("Rule Messages:: "+str(rule_msgs))

for rule in rule_msgs['changes']:
   	rule['mod_type'] = "remove"

print ("XRS_Test: Rule Msgs: %s" % rule_msgs)
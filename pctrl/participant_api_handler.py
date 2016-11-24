#!/usr/bin/env python
#  Author:
#  Florian Kaufmann (DE-CIX)

import json
import os
import sys
import time
import cgi
import collections
import BaseHTTPServer

################################################################################# - FileHandler (1)
class FileHandler(object):
    def __init__(self, container, ds_name):

        # file on drive
        self.filename = 'datastore.json'
        self.file = {}

        # read current file
        self.file = self.read()
        
        # override schema
        if ds_name == 'schema':
            self.write(container, ds_name)
        # do nothing if datastore exist
        elif self.checkKeyExist(self.file, ds_name):
            pass
        # new datastore
        else:
            self.write(container, ds_name)


    # check if ds_name exist in file
    def checkKeyExist(self, file, ds_name):
 
        check = False
        if isinstance(file, collections.Iterable):
            for key in file:
                if key == ds_name:
                    check = True
        return check

    # return file - or return named datastore in file 
    def read(self, ds_name=None):

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as outfile:
                try:
                    file = json.load(outfile)    
                except:
                    file = {}
                outfile.close()
        else:
            # create file
            open(self.filename, 'w').close()
            file = {}

        # if key not none and exist in file
        if ds_name != None and self.checkKeyExist(file, ds_name):
            return file[ds_name]
        else:
            return file

    # write file - or write named datastore in file
    def write(self, container, ds_name=None):          

        if os.path.exists(self.filename):
            with open(self.filename, 'w') as outfile:
                # if key not none create datastore in file
                if ds_name != None:
                    self.file[ds_name] = container
                    json.dump(self.file, outfile)
                else:
                    json.dump(container, outfile)
                outfile.close()


################################################################################# - DataStore (2)
class DataStore(object):
    def __init__(self, datastore, ds_protect):

        self.datastore = datastore
        self.pos_elements = ['inbound', 'outbound']

        if self.datastore in ds_protect:
            i_policy1 = {}
            i_policy1.update({"cookie" : 4097 })
            i_policy1.update({"match" : {"eth_src": "08:00:27:89:3b:9f", "ipv4_dst": "140.0.0.1", "udp_dst": 53} })
            i_policy1.update({"action" : {"drop": 0} })
            i_policy2 = {}
            i_policy2.update({"cookie" : 4098 })
            i_policy2.update({"match" : {"eth_src": "08:00:bb:bb:01:00", "ipv4_dst": "140.0.0.2", "udp_dst": 53} })
            i_policy2.update({"action" : {"drop": 0} })            
            inbound = {"inbound": [i_policy1, i_policy2]}

            o_policy = {}
            o_policy.update({"cookie" : 5 })
            o_policy.update({"match" : {"eth_dst": "08:00:27:89:3b:9f"} })
            o_policy.update({"action" : {"fwd": 3} })
            outbound = {"outbound": [o_policy]}
            
            self.container = (inbound, outbound)

        else:
            self.container = None
        
        self.filehandler = FileHandler(self.container, self.datastore)


    def checkSchema(self, recive, path):

        # open datastore file
        data = self.filehandler.read(self.datastore)
        pos_elements =  self.list_elements(data)
        
        # data store is empty
        if data is None or not data:
            return True

        # iterable - recive-element keys as re_key
        if isinstance(recive, collections.Iterable):
            for recive_element in recive:
                #/bh/ -> recive_element dict
                # check 1 to 3 arguments and right datastore
                if len(path) in range (1,4) and self.datastore == path[0] and isinstance(recive_element, dict):

                    # iterate over every recive element
                    for re_key in recive_element.keys():
                        
                        # recive element found in pos_data_elements
                        if re_key in pos_elements and re_key in self.pos_elements:

                            # create current cookie list
                            cookie_list = []
                            for data_element in data:
                                # if key from recive element exist in data element - fill cookie_list
                                if data_element.get(re_key):
                                    cookie_list = self.list_cookies(data_element.get(re_key))

                            # check every recive cookie with cookie_list
                            for subelement in recive_element[re_key]:
                                # cookie found
                                if 'cookie' in subelement.keys() and subelement['cookie'] in cookie_list:
                                    return False
                    # no same element and no same cookie found
                    return True

                else:
                    # len path not between 1 and 3 or wrong datastore or no dict'
                    return False

        else:
            # recive element not iterable
            return False


    def get(self, path):
       
        # open datastore file and index it
        data = self.filehandler.read(self.datastore)
        pos_elements =  self.list_elements(data)
        pos_path_list = self.list_elements_path(data)
        
        # empty data store
        if data is None or not data:
            return ((), pos_path_list)

        # only select datastore - return full data and next content
        if len(path) == 1 and self.datastore == path[0]:
            return (data, pos_path_list)

        # more information in url 
        if len(path) >= 2 and self.datastore == path[0]:
            # get first element from url
            check_element = path[1]

            # check element is a possible element
            if check_element in pos_elements:      

                
                # iterate over every element in datastore
                for data_element in data:
                    
                    # check element is in data element
                    # select element in datastore
                    if check_element in data_element.keys():

                        # create list with possible path [datastore'/'element'/'cookie']
                        pos_cookie_list = self.list_cookies_path(data_element[check_element], check_element)

                        # only select element - return with next content
                        if len(path) == 2:
                            return (data_element, pos_cookie_list)

                        # try to select a cookie
                        else:
                            cookie = None
                            # iterate over cookies
                            for subelement in data_element[check_element]:
                                if path[2].isdigit() and subelement['cookie'] == int(path[2]): # select cookie
                                    cookie = subelement
                           
                            # return cookie if exist
                            if cookie != None: 
                                return (cookie, pos_cookie_list)
                            else:
                            # build error if cookie not in data element
                                raise ValueError(404, pos_cookie_list)

            # raise error if element not a possible element            
            else:
                raise ValueError(404, pos_path_list)


    def post(self, recive ,path):
        
        data = self.filehandler.read(self.datastore)      
        pos_path_list = []

        # post data store
        if (data is None or not data) and self.datastore == path[0]:
            # write recive data to datastore
            self.filehandler.write(recive, self.datastore)
            # return created element list
            return self.list_elements_path(recive)

        # path len between 1 and 2 ['bh'] or ['bh','inbound']
        elif len(path) in range(1,3) and self.datastore == path[0]:

            # list of all keys from data elements
            data_list = []
            for data_element in data:
                data_list.extend(self.list_elements(data_element))

            # iterate over recive elements and element keys
            for recive_element in recive:
                for re_key in recive_element:

                    # if key exist in data
                    if re_key in data_list:
                        
                        # iterate over data
                        for data_element in data:
                            # extend data with recive information
                            if data_element.get(re_key) and recive_element.get(re_key):
                                data_element.get(re_key).extend(recive_element.get(re_key))

                    # if key not exist in data, append complete element
                    else:
                        data.append(recive_element)

                    # extend pos_path_list for every recived cookie
                    pos_path_list.extend(self.list_cookies_path(recive_element[re_key], re_key))
       
        else:
            return pos_path_list

        # write data in data store and return path list
        self.filehandler.write(data, self.datastore)
        return pos_path_list


    def delete(self, path): #documentation
        
        # delete complete data store
        if len(path) == 1 and self.datastore == path[0]:
            self.filehandler.write((), self.datastore)
        
        else:
            if len(path) >= 2 and self.datastore == path[0]:
                # open datastore file and index it
                data = self.filehandler.read(self.datastore)
                pos_path_list = []
                del_flag = False

                # iterate over every data element
                for data_element in data: 
                    
                    # if data element found remove it
                    if data_element.get(path[1]):
                        if len(path) == 2:
                            data.remove(data_element)
                            del_flag = True

                        # remove only a cookie
                        if len(path) == 3:
                            # iterate over every cookie
                            for subelement in data_element.get(path[1]):
                                
                                # if cookie found remove it
                                if str(subelement['cookie']) == path[2]:
                                    data_element.get(path[1]).remove(subelement)
                                    del_flag = True

                                    # if data element is now empty remove complete element
                                    if data_element.get(path[1]) is None or not data_element.get(path[1]):
                                        data.remove(data_element)
                    
                
                # fill pos_path_list with elements after delete
                for data_element in data:
                    if len(path) == 2:
                        pos_path_list = self.list_elements_path(data_element)
                    elif len(path) == 3:
                        if data_element.get(path[1]):
                            pos_path_list.extend(self.list_cookies_path(data_element[path[1]], path[1]))

                # write data in datastore if something is deleted
                if del_flag:
                    self.filehandler.write(data, self.datastore)
                    return pos_path_list
                
                # nothing deleted
                else:
                    raise ValueError()
            # wrong datastore
            else:
                raise ValueError()


    def list_elements(self, elements):
        element_list = []
        if isinstance(elements, list):
            for element in elements:
                    for key in element.keys():
                        element_list.append(key)
        elif isinstance(elements, dict):
             for key in elements.keys():
                        element_list.append(key)
        return element_list

    def list_elements_path(self, elements):
        element_path = []
        element_list = self.list_elements(elements)
        for element in element_list:
            element_path.append(self.datastore+'/'+element)
        return element_path

    def list_cookies(self, element):
        cookie_list = []
        for subelement in element:
            cookie_list.append(subelement['cookie'])
        return cookie_list

    def list_cookies_path(self, element, check_element):
        cookie_path = []
        cookie_list = self.list_cookies(element)
        for cookie in cookie_list:
            cookie_path.append(self.datastore+'/'+check_element+'/'+str(cookie))
        return cookie_path

################################################################################# - ApiHandler (3)
class ApiHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    # create data stores
    ds_names = ['bh', 'schema']
    ds_protect = ['schema']
    ds = {}
    for name in ds_names:
        ds[name] = DataStore(name, ds_protect)


    def do_HEAD(self):
        self.send_response(501) # not implemented
        self.response_entrance()


    def do_GET(self):
        # get parsed path
        parsed_path = self.parse_path()         

        # check 1 to 3 arguments and right datastore
        if len(parsed_path) in range(1,4) and parsed_path[0] in self.ds_names: 
            
            try:
                # get elements and next content locations (elements, cookies)
                element, next_content_location = self.ds[parsed_path[0]].get(parsed_path)
                self.send_response(200) # ok
                self.send_header('Content-type', 'application/json')
                # element is empty
                if element is None or not element:
                    self.response_entrance()
                else:
                    self.response_next_content_location(next_content_location)
                # response data element/cookie
                self.wfile.write(json.dumps (element))
            
            # handle value error if no data available - return available locations
            # error def: ['http-response-code', 'list of available content locations']
            except ValueError as e:
                self.send_response(int(e[0]))
                self.response_next_content_location(e[1])

        # wrong datastore (first url parameter) - return available locations
        elif len(parsed_path) in range(1,4) and parsed_path[0] not in self.ds_names:
            self.send_response(400) # bad request
            self.response_entrance()

        # path length not between 1 and 3
        else:
            self.handle_path(parsed_path)   


    def do_POST(self):
        # get parsed path
        parsed_path = self.parse_path()  

        # load data
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'application/json':
            data = None
            length = int(self.headers.getheader('content-length'))
            if length != 0:
                try:
                    data = json.loads(self.rfile.read(length))
                except:
                    self.send_response(400) # bad request

        # check 1 to 3 arguments and right datastore
        if len(parsed_path) in range(1,4) and parsed_path[0] in self.ds_names: 

            # error because no cookie selection or protected data store for post
            if len(parsed_path) == 3 or parsed_path[0] in self.ds_protect:
                self.method_not_allowed(parsed_path)

            else:
                if len(parsed_path) == 2 and isinstance(data, dict):
                   # pack element(dict) in a list if parsed path ['bh', 'inbound']
                   data = [data]

                # continue with next if block
                if self.ds[parsed_path[0]].checkSchema(data, parsed_path) and isinstance(data, list):
                    # post data and response next content location 
                    next_content_location = self.ds[parsed_path[0]].post(data, parsed_path)
                    self.send_response(201) # created
                    self.response(next_content_location)
                else:
                    # schema check false - key already exist or data is no list
                    self.send_response(400) # bad request

        # wrong datastore (first url parameter) - return available locations
        elif len(parsed_path) in range(1,4) and parsed_path[0] not in self.ds_names:
            self.send_response(400) # bad request
            self.response_entrance()

        # path length not between 1 and 3
        else:
            self.handle_path(parsed_path)   


    def do_DELETE(self):
        # get parsed path
        parsed_path = self.parse_path()

        #['bh', 'inbound', '4098']
        # check 1 to 3 arguments and right datastore
        if len(parsed_path) in range(1,4) and parsed_path[0] in self.ds_names: 
            # error because no protected data store for delete
            if parsed_path[0] in self.ds_protect:
                self.method_not_allowed(parsed_path)
            else:
                try:
                    # call delete function
                    next_content_location = self.ds[parsed_path[0]].delete(parsed_path)
                    self.send_response(200) # ok
                    self.response(next_content_location)
                except:
                    self.send_response(400) # bad request

        # path length not between 1 and 3
        else:
            self.handle_path(parsed_path)   


    def do_PUT(self):
        self.send_response(501) # not implemented
        self.response_entrance()

    def parse_path(self):
        # parse url in array ['bh', 'inbound', '4097'] etc.
        # url def: ['datastore', 'element', 'cookie']
        parsed_path = self.path.split('/')
        return filter(None, parsed_path) 

    def method_not_allowed(self, parsed_path):
        self.send_response(405) # method not allowed
        try:
            element, next_content_location = self.ds[parsed_path[0]].get(parsed_path)
        except ValueError as e:
            next_content_location = e[1]
        # send only allow GET and next content location
        self.send_header('Allow', 'GET')
        self.response_next_content_location(next_content_location)

    def handle_path(self, parsed_path):
        # no path given - return content locations (datastores)
        if len(parsed_path) == 0:
            self.send_response(303) # see other
            self.response_next_content_location(self.ds_names)
        # error, url path to long
        elif len(parsed_path) >=4:
            self.send_response(414) # url to long
        # other errors
        else:
            self.send_response(500) # internal server error

    def response_entrance(self):
        # send api entrance by default
        location = 'http://'+str(self.server.server_name)+':'+str(self.server.server_port)
        self.send_header('Location', location)
        self.response_next_content_location(self.ds_names)

    def response_next_content_location(self, ncl):
        #  send next content location by default
        for next_content in ncl:
            self.send_header('Content-location','/'+next_content)
        self.end_headers()

    def response(self, next_content_location):
        # no location given or empty
        print next_content_location
        if next_content_location is None or not next_content_location:
            self.response_entrance()
        else:
            self.response_next_content_location(next_content_location)

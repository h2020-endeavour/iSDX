# pctrl - Participants' SDX Controller

This module is in charge of running an `event handler` for each SDX participant. This `event handler`
receives network events from `xrs` module (BGP updates), `arproxy` module (ARP requests), and participants's
control interface (high-level policy changes). It processes incoming network events to generate new
BGP announcements and data plane updates. It sends the BGP announcements to the `xrs` module and
dp updates to the `flanc` module. 

See examples/test-ms/README.md for an example of how to run pctrl along with everything else.


&nbsp;


# Participants' API

This module is for high-level policy changes through the `event handler` for each SDX participant.
It start automatically with the participant controller with the parameter ***ip_participant_controller*** 
and ***api_port*** stored in sdx_global.cfg.
```
	"Participants": {
	    "1": {
	        "EH_SOCKET": [
	                "localhost", 
	                5551
	            ] ...
	    },
	    "2": {
	        "EH_SOCKET": [
	                "localhost", 
	                5552
	            ] ...
	    },
	    "3": {
	        "EH_SOCKET": [
	                "localhost", 
	                5553
	            ] ...
	    }  
	} ...
```
**localhost** will bind on every interface (0.0.0.0) on virtual machine. The port forwarding in vagrant makes it
possible to use the api also at the host machine.

&nbsp;


---
> **Introduction** to use the api generally.

+ API GET
```
	curl -vX GET http://ip_participant_controller:api_port/

e.g.	curl -vX GET http://localhost:5551/
```


+ API RESPONSE

```
	Status: 303 see other
	Content-Location: /bh, /schema
```

The ***/schema*** service is a section with prefilled policys. It is used in the following blackholing example.
The commands POST and DELETE not allowed on the  ***/schema*** service.


&nbsp;


+ Response Header

```
Status          	Satus of the HTTP response. (see Status/Error Codes)
Content-Type 		The MIME type of this content. (e.g. application/json)
Content-Location	An alternate location for the returned data. (e.g. /bh/inbound)
Location         	Used in redirection. (e.g. in case of wrong request, response correct url)
```


&nbsp;


+ Status/Error Codes

|Code|Meaning|Explanation|
|---|---|---|
|200|ok|a  valid get/delete|
|201|created|a valid post, policy successful created|
|303|see other|need to specify uri|
|400|bad request|an invalid get/post/delete|
|404|not found|service or uri not found|
|405|method not allowed|e.g. post/delete on schema service not allowed| 
|409|conflict|e.g. cookie already exist on post or is wrong formated| 
|414|url to long|use instead service/element/subelement (e.g. bh/inbound/4097)| 
|500|internal server error|all other errors| 
|501|not implemented|put/head are not implemented| 


&nbsp;


+ API DELETE
```
1)	curl -vX DELETE http://ip_participant_controller:api_port/service1/element1/subelement1
2)	curl -vX DELETE http://ip_participant_controller:api_port/service1/element1
3)	curl -vX DELETE http://ip_participant_controller:api_port/service1/
```


+ API RESPONSE

```
	Status: 200 OK
1)	Content-Location: other possible subelements (e.g. service1/element1/subelement2, ..)
2)	Content-Location: other possible elements (e.g. service1/element2, service1/element3)
3)	Content-Location: /service1, /service2
```

You can not delete a complete service but all data within the service. After api DELETE 3) the data from **service1** is empty.
The api GET ***/service1*** response only [].


&nbsp;


+ API POST
```
1)	curl -vX POST -H 'Content-Type: application/json' -d 'data1' http://ip_participant_controller:api_port/service1/
2)	curl -vX POST -H 'Content-Type: application/json' -d 'data2' http://ip_participant_controller:api_port/service1/element1
```
**data1** contains a list of elements (e.g. inbound, outbound..) with subelements (cookies) like the response from api GET ***/service1***. 

**data2** contains a single element (e.g. inbound) also with subelements (cookies) like the response from api GET ***/service1/element1/***.

+ API RESPONSE

```
	Status: 201 Created
	Content-Location: /service1/element1/subelement1
	Content-Location: /service1/element1/subelement2
```
The response for API POST 1) and 2) are the same, it returns the created cookie`s URI.


&nbsp;


&nbsp;


---
> **TORCH** implementation (process to controller)

The api uses a ***datastore.json*** to store policys locally on the participant controller. After each test, the datastore
will be deleted (defined in startup.sh and clean.py). The ***blackholing*** commands in **torch use only inbound policys** for insert/remove commands.
The chart below gives an example for the current possible commands in the torch blackholing implementation.


|API|URI|Explanation|
|---|---|---|
|GET|/bh/|shows all policys|
||/bh/inbound/|shows only inbound policys|
||/bh/inbound/4097/|shows only inbound cookie 4097|
|DELETE|/bh/|only inbound policys **from controller** will be deleted<br>(e.g. outbound will also be deleted in api)|
||/bh/inbound/|deletes all inbound policys|
||/bh/inbound/4097/|deletes only inbound cookie 4097|
|POST|/bh/|**only inbound** policys will be pushed **to controller**<br>if exist, outbound policys will be stored in api<br>(e.g. schema from GET /bh/)|
||/bh/inbound/|push list of inbound policys **to controller**<br>(e.g. schema from GET /bh/inbound/)|
||/bh/inbound/4097/|not implemented|


&nbsp;


&nbsp;


---
> **Blackholing** prefilled with the stored /schema example

+ API GET
		
```
1)	curl -X GET http://ip_participant_controller:api_port/bh/
2)	curl -X GET http://ip_participant_controller:api_port/bh/inbound
3)	curl -X GET http://ip_participant_controller:api_port/bh/inbound/4097
```

+ Response 1 (All Blackholing Policys)
```
	[
	    {
	        "inbound": [
	            {
	                "action": {
	                    "drop": 0
	                },
	                "cookie": 4097,
	                "match": {
	                    "eth_src": "08:00:27:89:3b:9f",
	                    "udp_dst": 53,
	                    "ipv4_dst": "140.0.0.1"
	                }
	            },
	            {
	                "action": {
	                    "drop": 0
	                },
	                "cookie": 4098,
	                "match": {
	                    "eth_src": "08:00:bb:bb:01:00",
	                    "udp_dst": 53,
	                    "ipv4_dst": "140.0.0.2"
	                }
	            }
	        ]
	    },
	    {
	        "outbound": [
	            {
	                "action": {
	                    "fwd": 3
	                },
	                "cookie": 5,
	                "match": {
	                    "eth_dst": "08:00:27:89:3b:9f"
	                }
	            }
	        ]
	    }
	]

	Status: 200 OK
	Content-Type: applicatiopn/json
	Content-Location: /bh/inbound, /bh/outbound
```


+ Response 2 (Only Inbound Blackholing Policys)

```
	{
	    "inbound": [
	        {
	            "action": {
	                "drop": 0
	            },
	            "cookie": 4097,
	            "match": {
	                "eth_src": "08:00:27:89:3b:9f",
	                "udp_dst": 53,
	                "ipv4_dst": "140.0.0.1"
	            }
	        },
	        {
	            "action": {
	                "drop": 0
	            },
	            "cookie": 4098,
	            "match": {
	                "eth_src": "08:00:bb:bb:01:00",
	                "udp_dst": 53,
	                "ipv4_dst": "140.0.0.2"
	            }
	        }
	    ]
	}

	Status: 200 OK
	Content-Type: applicatiopn/json
	Content-Location: /bh/inbound/4097, /bh/outbound/4098
```

+ Response 3 (Only Inbound Cookie 4097)
```
	{
	    "action": {
	        "drop": 0
	    },
	    "cookie": 4097,
	    "match": {
	        "eth_src": "08:00:27:89:3b:9f",
	        "udp_dst": 53,
	        "ipv4_dst": "140.0.0.1"
	    }
	}

	Status: 200 OK
	Content-Type: applicatiopn/json
	Content-Location: /bh/inbound/4097, /bh/inbound/4098
```


&nbsp;


+ API DELETE
```
1)	curl -vX DELETE http://ip_participant_controller:api_port/bh/inbound/4097

2)	curl -vX DELETE http://ip_participant_controller:api_port/bh/inbound

3)	curl -vX DELETE http://ip_participant_controller:api_port/bh/
```


+ API RESPONSE

```
1)	Status: 200 OK
	Content-Location: /bh/inbound/4098, /bh/inbound/4099

2)	Status: 200 OK
	Content-Location: /bh/outbound/

3)	Status: 200 OK
	Location: http://ip_participant_controller:api_port/
	Content-Location: /bh, /schema
```


&nbsp;


+ API POST
		
```
1)	curl -X POST -H 'Content-Type: application/json' -d '[{"inbound": [{"action": {"drop": 0}, "cookie": 4097, "match": {"eth_src": "08:00:bb:bb:01:00", "udp_dst": 53, "ipv4_dst": "140.0.0.1"}}]}]' http://localhost:5553/bh/

2)	curl -X POST -H 'Content-Type: application/json' -d '{"action": {"drop": 0},"cookie": 4098,"match": {"eth_src": "08:00:bb:bb:01:00","udp_dst": 53,"ipv4_dst": "140.0.0.2"}}' http://localhost:5553/bh/inbound/
```


+ API RESPONSE

```
1)	Status: 201 CREATED
	Content-Location: /bh/inbound/4097

2)	Status: 201 CREATED
	Content-Location: /bh/inbound/4098
```
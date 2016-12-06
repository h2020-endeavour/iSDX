# pctrl - Participants' SDX Controller

This module is in charge of running an `event handler` for each SDX participant. This `event handler`
receives network events from `xrs` module (BGP updates), `arproxy` module (ARP requests), and participants's
control interface (high-level policy changes). It processes incoming network events to generate new
BGP announcements and data plane updates. It sends the BGP announcements to the `xrs` module and
dp updates to the `flanc` module. 

See examples/test-ms/README.md for an example of how to run pctrl along with everything else.


&nbsp;


# participant_api - Participants' API

This module is for high-level policy changes through the `event handler` for each SDX participant.

***ip_participant_controller*** and ***api_port*** stored in sdx_global.cfg
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


&nbsp;


---
> ***Introduction***
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


&nbsp;


+ Possible Response Headers

```
Status          	Satus of the HTTP response. (see Status/Error Codes)
Content-Type 		The MIME type of this content. (e.g. application/json)
Content-Location	An alternate location for the returned data. (e.g. /bh/inbound)
Location         	Used in redirection. (e.g. in case of wrong request, response correct url)
```

+ Status/Error Codes

|Code|Meaning|Explanation|
|---|---|---|
|200|ok|a  valid get/delete|
|201|created|a valid post, policy successful created|
|303|see other|need to specify uri|
|400|bad request|an invalid get/post/delete|
|404|not found|service or content not found|
|405|method not allowed|e.g. post/delete on schema service not allowed| 
|409|conflict|json already exist on post or is wrong formated| 
|414|url to long| use instead service/element/subelement (e.g. bh/inbound/4097)| 
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

You can`t delete a complete service but all data within the service. After API DELETE 3) the data from service1 is empty.
The GET on service1 will response [].

&nbsp;


---
> ***Blackholing (schema example)***

+ API GET
		
```
	curl -X GET http://ip_participant_controller:api_port/bh/
	curl -X GET http://ip_participant_controller:api_port/bh/inbound
	curl -X GET http://ip_participant_controller:api_port/bh/inbound/4097
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



DELETE



POST

+ API POST
		
```
	curl -X POST --header ‘Content-Type: application/json' -d '{"inbound": [{"action": {"drop": 0}, "cookie": 4097, "match": {"eth_src": "08:00:bb:bb:01:00", "udp_dst": 53, "ipv4_dst": "140.0.0.1"}}]}' http://localhost:5553/bh/
```










&nbsp;


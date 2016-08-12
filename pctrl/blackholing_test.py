{
  "policy": [
    
    {
      "remove": [
        
        {
          "inbound": [
            {
              "cookie": 3,
              "match": {
                "eth_src": "08:00:27:89:3b:9f"
              },
              "action": {
                "drop": 0
              }
            }
          ]
        }


      ]
    },
    
    {
      "insert": [
        
        {
          "inbound": [
            
            {
              "cookie": 3,
              "match": {
                "eth_src": "08:00:27:89:3b:99"
              },
              "action": {
                "drop": 0
              }
            }
          ]
        }


      ]
    }
  

  ]
}
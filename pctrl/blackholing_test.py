{
  "policy": [
    {
      "removal_cookies": [
        {
          "cookie": 57,
          "match": {
            "tcp_dst": 1111
          },
          "action": {
            "fwd": 0
          }
        },

        {
          "cookie": 58,
          "match": {
            "tcp_dst": 1111
          },
          "action": {
            "fwd": 1
          }
        },

        {
          "cookie": 59,
          "match": {
            "tcp_dst": 1111
          },
          "action": {
            "fwd": 1
          }
        }

      ]
    },
    {
      "new_policies": [
        {
          "cookie": 1,
          "match": {
            "tcp_dst": 4323
          },
          "action": {
            "fwd": 0
          }
        },
        {
          "cookie": 2,
          "match": {
            "tcp_dst": 4324
          },
          "action": {
            "fwd": 1
          }
        },
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
}
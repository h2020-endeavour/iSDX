{
  "id": 2,
  "title": "blackholing-demo",
  "originalTitle": "blackholing-demo",
  "tags": [],
  "style": "dark",
  "timezone": "browser",
  "editable": true,
  "hideControls": false,
  "sharedCrosshair": false,
  "rows": [
    {
      "collapse": false,
      "editable": true,
      "height": "350px",
      "panels": [
        {
          "aliasColors": {
            "Port A-In": "#7EB26D",
            "Port B-In": "#EAB839",
            "Port B-Out": "#AEA2E0",
            "port_packets_out.non_negative_derivative": "#AEA2E0"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 9,
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Port A-In",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_packets_in",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "A"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ]
            },
            {
              "alias": "Port B-In",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_packets_in",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Port C-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_packets_out",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                }
              ]
            },
            {
              "alias": "Port B-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_packets_out",
              "policy": "default",
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Port Statistics",
          "tooltip": {
            "msResolution": true,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Packets",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        },
        {
          "aliasColors": {
            "Port A-In": "#7EB26D",
            "Port B-In": "#EAB839",
            "Port B-Out": "#AEA2E0"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 8,
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Port A-In",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "port_bytes_in",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "A"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ]
            },
            {
              "alias": "Port B-In",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "port_bytes_in",
              "policy": "default",
              "query": "SELECT last(\"value\") FROM \"flow_packet_count\" WHERE \"cookie\" = '196610' AND \"dp_name\" = 'Edge-1' AND $timeFilter GROUP BY time(10s) fill(0)",
              "rawQuery": false,
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Port C-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "port_bytes_out",
              "policy": "default",
              "refId": "E",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                }
              ]
            },
            {
              "alias": "Port B-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "null"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_bytes_out",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Port Statistics",
          "tooltip": {
            "msResolution": true,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "Bps",
              "label": "Bytes",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        }
      ],
      "title": "New row"
    },
    {
      "collapse": false,
      "editable": true,
      "height": "350px",
      "panels": [
        {
          "aliasColors": {
            "Drop Rule": "#E24D42",
            "Drop Rule (Sum)": "#E24D42"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 7,
          "interval": ">2s",
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Drop Rule - Participant A (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "flow_packet_count",
              "policy": "default",
              "query": "SELECT non_negative_derivative(last(\"value\"), 10s) FROM \"flow_packet_count\" WHERE \"cookie\" = '196613' AND \"dp_name\" = 'Edge-1' AND $timeFilter GROUP BY time(10s) fill(0)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ]
            },
            {
              "alias": "Drop Rule - Participant B",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "flow_packet_count",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Drop Rule (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "flow_packet_count",
              "policy": "default",
              "query": "SELECT non_negative_derivative(sum(\"value\"), 10s) FROM \"flow_packet_count\" WHERE \"eth_src\" = '08:00:bb:bb:01:00' AND \"dp_name\" = 'Edge-1' OR \"eth_src\" = '08:00:bb:bb:02:00' AND \"dp_name\" = 'Edge-2' AND $timeFilter GROUP BY time(10s) fill(0)",
              "rawQuery": false,
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Blackholing Policy",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Packets",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        },
        {
          "aliasColors": {
            "Drop Rule": "#E24D42",
            "Drop Rule (Sum)": "#E24D42"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 14,
          "interval": ">2s",
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Drop Rule - Participant A (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "flow_byte_count",
              "policy": "default",
              "query": "SELECT non_negative_derivative(last(\"value\"), 10s) FROM \"flow_packet_count\" WHERE \"cookie\" = '196613' AND \"dp_name\" = 'Edge-1' AND $timeFilter GROUP BY time(10s) fill(0)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ]
            },
            {
              "alias": "Drop Rule - Participant B",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "flow_byte_count",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Drop Rule (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "0"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "flow_byte_count",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Blackholing Policy",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "Bps",
              "label": "Bytes",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        }
      ],
      "title": "New row"
    },
    {
      "collapse": false,
      "editable": true,
      "height": "350px",
      "panels": [
        {
          "aliasColors": {
            "Drop Rule": "#E24D42",
            "Drop Rule (Sum)": "#E24D42",
            "Port A+B-In": "#EF843C",
            "Port A+B-In (Sum)": "#EF843C",
            "Port B+C-Out (Sum)": "#6ED0E0",
            "Port C-Out": "#6ED0E0"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 13,
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Port A+B-In (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "hide": false,
              "measurement": "port_packets_in",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "A"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Port C-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_packets_out",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                }
              ]
            },
            {
              "alias": "Drop Rule (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "flow_packet_count",
              "policy": "default",
              "refId": "D",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Port Statistics (Sum)",
          "tooltip": {
            "msResolution": true,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "short",
              "label": "Packets",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        },
        {
          "aliasColors": {
            "Drop Rule (Sum)": "#E24D42",
            "Port A+B-In": "#EF843C",
            "Port A+B-In (Sum)": "#EF843C",
            "Port C-Out": "#6ED0E0"
          },
          "bars": false,
          "datasource": null,
          "editable": true,
          "error": false,
          "fill": 1,
          "grid": {
            "threshold1": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2": null,
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "id": 11,
          "isNew": true,
          "legend": {
            "avg": false,
            "current": false,
            "max": false,
            "min": false,
            "show": true,
            "total": false,
            "values": false
          },
          "lines": true,
          "linewidth": 2,
          "links": [],
          "nullPointMode": "connected",
          "percentage": false,
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "span": 6,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "alias": "Port A+B-In (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_bytes_in",
              "policy": "default",
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "A"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            },
            {
              "alias": "Port C-Out",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "port_bytes_out",
              "policy": "default",
              "refId": "B",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "last"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                }
              ]
            },
            {
              "alias": "Drop Rule (Sum)",
              "dsType": "influxdb",
              "groupBy": [
                {
                  "params": [
                    "10s"
                  ],
                  "type": "time"
                },
                {
                  "params": [
                    "none"
                  ],
                  "type": "fill"
                }
              ],
              "measurement": "flow_byte_count",
              "policy": "default",
              "refId": "C",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "params": [
                      "value"
                    ],
                    "type": "field"
                  },
                  {
                    "params": [],
                    "type": "sum"
                  },
                  {
                    "params": [
                      "10s"
                    ],
                    "type": "non_negative_derivative"
                  }
                ]
              ],
              "tags": [
                {
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:01:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "OR",
                  "key": "eth_src",
                  "operator": "=",
                  "value": "08:00:bb:bb:02:00"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Port Statistics (Sum)",
          "tooltip": {
            "msResolution": true,
            "shared": true,
            "value_type": "cumulative"
          },
          "type": "graph",
          "xaxis": {
            "show": true
          },
          "yaxes": [
            {
              "format": "Bps",
              "label": "Bytes",
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            },
            {
              "format": "short",
              "label": null,
              "logBase": 1,
              "max": null,
              "min": null,
              "show": true
            }
          ]
        }
      ],
      "title": "New row"
    }
  ],
  "time": {
    "from": "now-15m",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "templating": {
    "list": []
  },
  "annotations": {
    "list": []
  },
  "refresh": "5s",
  "schemaVersion": 12,
  "version": 10,
  "links": []
}
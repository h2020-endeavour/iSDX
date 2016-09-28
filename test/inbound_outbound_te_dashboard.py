{
  "id": null,
  "title": "Inbound/Outbound TE",
  "originalTitle": "Inbound/Outbound TE",
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
      "height": "250px",
      "panels": [
        {
          "aliasColors": {},
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
          "id": 12,
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
              "alias": "dst-port:80",
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
              "measurement": "flow_packet_count",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "1"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            },
            {
              "alias": "dst-port:4321",
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
              "measurement": "flow_packet_count",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "2"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            },
            {
              "alias": "dst-port:4322",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "3"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Traffic generated from A",
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
          "aliasColors": {},
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
              "alias": "dst-port:80",
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
              "measurement": "flow_byte_count",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "1"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            },
            {
              "alias": "dst-port:4321",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "2"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            },
            {
              "alias": "dst-port:4322",
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
                  "key": "cookie",
                  "operator": "=",
                  "value": "3"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                },
                {
                  "condition": "AND",
                  "key": "table_id",
                  "operator": "=",
                  "value": "0"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Traffic generated from A",
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
      "title": "Row"
    },
    {
      "collapse": false,
      "editable": true,
      "height": "250px",
      "panels": [
        {
          "aliasColors": {},
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
              "alias": "B",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                }
              ]
            },
            {
              "alias": "C1",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                }
              ]
            },
            {
              "alias": "C2",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 4"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Traffic received by the IXP members",
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
          "aliasColors": {},
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
          "id": 15,
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
              "alias": "B",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-2"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "B"
                }
              ]
            },
            {
              "alias": "C1",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 3"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                }
              ]
            },
            {
              "alias": "C2",
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
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge 4"
                },
                {
                  "condition": "AND",
                  "key": "port_name",
                  "operator": "=",
                  "value": "C"
                }
              ]
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Traffic received by the IXP members",
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
      "height": "250px",
      "panels": [],
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
  "version": 5,
  "links": []
}
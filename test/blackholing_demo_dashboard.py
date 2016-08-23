{
  "id": 2,
  "title": "iSDX-beta",
  "originalTitle": "iSDX-beta",
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
      "height": "300px",
      "panels": [
        {
          "title": "Packet Counts",
          "error": false,
          "span": 6,
          "editable": true,
          "type": "graph",
          "isNew": true,
          "id": 9,
          "targets": [
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "A",
              "measurement": "port_packets_in",
              "alias": "Port A-In"
            },
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "B",
              "measurement": "port_packets_in",
              "alias": "Port B-In"
            },
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "C",
              "measurement": "port_packets_out",
              "alias": "Port C-Out"
            }
          ],
          "datasource": null,
          "renderer": "flot",
          "yaxes": [
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            },
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            }
          ],
          "xaxis": {
            "show": true
          },
          "grid": {
            "threshold1": null,
            "threshold2": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "lines": true,
          "fill": 1,
          "linewidth": 2,
          "points": false,
          "pointradius": 5,
          "bars": false,
          "stack": false,
          "percentage": false,
          "legend": {
            "show": true,
            "values": false,
            "min": false,
            "max": false,
            "current": false,
            "total": false,
            "avg": false
          },
          "nullPointMode": "connected",
          "steppedLine": false,
          "tooltip": {
            "value_type": "cumulative",
            "shared": true,
            "msResolution": true
          },
          "timeFrom": null,
          "timeShift": null,
          "aliasColors": {},
          "seriesOverrides": [],
          "links": []
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
                    "params": [],
                    "type": "difference"
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
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
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
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "E",
              "measurement": "port_bytes_out",
              "alias": "Port C-Out",
              "hide": false
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Byte Counts",
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
              "label": null,
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
      "height": "300px",
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
              "alias": "Drop Rule",
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
              "policy": "default",
              "query": "SELECT difference(last(\"value\")) FROM \"port_bytes_out\" WHERE \"port_name\" = 'A' AND $timeFilter GROUP BY time($interval) fill(null)",
              "rawQuery": false,
              "refId": "A",
              "resultFormat": "time_series",
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "non_negative_derivative",
                    "params": [
                      "10s"
                    ]
                  }
                ]
              ],
              "tags": [
                {
                  "key": "cookie",
                  "operator": "=",
                  "value": "196613"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ],
              "measurement": "flow_packet_count"
            }
          ],
          "timeFrom": null,
          "timeShift": null,
          "title": "Packet Count",
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
              "format": "bytes",
              "label": null,
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
          "title": "Byte Count",
          "error": false,
          "span": 6,
          "editable": true,
          "type": "graph",
          "isNew": true,
          "id": 10,
          "targets": [
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
              "tags": [
                {
                  "key": "cookie",
                  "operator": "=",
                  "value": "196613"
                },
                {
                  "condition": "AND",
                  "key": "dp_name",
                  "operator": "=",
                  "value": "Edge-1"
                }
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "0"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "non_negative_derivative",
                    "params": [
                      "10s"
                    ]
                  }
                ]
              ],
              "refId": "A",
              "measurement": "flow_byte_count",
              "alias": "Drop Rule"
            }
          ],
          "datasource": null,
          "renderer": "flot",
          "yaxes": [
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            },
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            }
          ],
          "xaxis": {
            "show": true
          },
          "grid": {
            "threshold1": null,
            "threshold2": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "lines": true,
          "fill": 1,
          "linewidth": 2,
          "points": false,
          "pointradius": 5,
          "bars": false,
          "stack": false,
          "percentage": false,
          "legend": {
            "show": true,
            "values": false,
            "min": false,
            "max": false,
            "current": false,
            "total": false,
            "avg": false,
            "alignAsTable": false,
            "rightSide": false,
            "hideEmpty": false
          },
          "nullPointMode": "null",
          "steppedLine": false,
          "tooltip": {
            "value_type": "individual",
            "shared": true,
            "msResolution": true
          },
          "timeFrom": null,
          "timeShift": null,
          "aliasColors": {},
          "seriesOverrides": [],
          "links": []
        }
      ],
      "title": "New row"
    },
    {
      "title": "New row",
      "height": "300px",
      "editable": true,
      "collapse": false,
      "panels": [
        {
          "title": "Packet Count",
          "error": false,
          "span": 6,
          "editable": true,
          "type": "graph",
          "isNew": true,
          "id": 12,
          "targets": [
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "sum",
                    "params": []
                  },
                  {
                    "type": "non_negative_derivative",
                    "params": [
                      "10s"
                    ]
                  }
                ]
              ],
              "refId": "A",
              "measurement": "port_packets_in",
              "alias": "Port A+B-In"
            },
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "B",
              "alias": "Port C-Out",
              "measurement": "port_packets_out"
            }
          ],
          "datasource": null,
          "renderer": "flot",
          "yaxes": [
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            },
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            }
          ],
          "xaxis": {
            "show": true
          },
          "grid": {
            "threshold1": null,
            "threshold2": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "lines": true,
          "fill": 1,
          "linewidth": 2,
          "points": false,
          "pointradius": 5,
          "bars": false,
          "stack": false,
          "percentage": false,
          "legend": {
            "show": true,
            "values": false,
            "min": false,
            "max": false,
            "current": false,
            "total": false,
            "avg": false
          },
          "nullPointMode": "connected",
          "steppedLine": false,
          "tooltip": {
            "value_type": "cumulative",
            "shared": true,
            "msResolution": true
          },
          "timeFrom": null,
          "timeShift": null,
          "aliasColors": {},
          "seriesOverrides": [],
          "links": []
        },
        {
          "title": "Byte Count",
          "error": false,
          "span": 6,
          "editable": true,
          "type": "graph",
          "isNew": true,
          "id": 11,
          "targets": [
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "sum",
                    "params": []
                  },
                  {
                    "type": "non_negative_derivative",
                    "params": [
                      "10s"
                    ]
                  }
                ]
              ],
              "refId": "A",
              "measurement": "port_bytes_in",
              "alias": "Port A+B-In"
            },
            {
              "policy": "default",
              "dsType": "influxdb",
              "resultFormat": "time_series",
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
              ],
              "groupBy": [
                {
                  "type": "time",
                  "params": [
                    "10s"
                  ]
                },
                {
                  "type": "fill",
                  "params": [
                    "null"
                  ]
                }
              ],
              "select": [
                [
                  {
                    "type": "field",
                    "params": [
                      "value"
                    ]
                  },
                  {
                    "type": "last",
                    "params": []
                  },
                  {
                    "type": "difference",
                    "params": []
                  }
                ]
              ],
              "refId": "B",
              "alias": "Port C-Out",
              "measurement": "port_bytes_out"
            }
          ],
          "datasource": null,
          "renderer": "flot",
          "yaxes": [
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            },
            {
              "label": null,
              "show": true,
              "logBase": 1,
              "min": null,
              "max": null,
              "format": "short"
            }
          ],
          "xaxis": {
            "show": true
          },
          "grid": {
            "threshold1": null,
            "threshold2": null,
            "threshold1Color": "rgba(216, 200, 27, 0.27)",
            "threshold2Color": "rgba(234, 112, 112, 0.22)"
          },
          "lines": true,
          "fill": 1,
          "linewidth": 2,
          "points": false,
          "pointradius": 5,
          "bars": false,
          "stack": false,
          "percentage": false,
          "legend": {
            "show": true,
            "values": false,
            "min": false,
            "max": false,
            "current": false,
            "total": false,
            "avg": false
          },
          "nullPointMode": "connected",
          "steppedLine": false,
          "tooltip": {
            "value_type": "cumulative",
            "shared": true,
            "msResolution": true
          },
          "timeFrom": null,
          "timeShift": null,
          "aliasColors": {},
          "seriesOverrides": [],
          "links": []
        }
      ]
    }
  ],
  "time": {
    "from": "2016-08-23T14:53:40.284Z",
    "to": "2016-08-23T14:58:31.811Z"
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
  "refresh": false,
  "schemaVersion": 12,
  "version": 4,
  "links": []
}
# generate network equivalent to generic test-mh
# 3 participants
# combination of inbound and outbound rules
# additional test for unmatched traffic on port 8888

mode multi-hop
participants 3
peers 1 2 3

participant 1 100 edge-1:5 MAC 172.0.0.1/16
participant 2 200 edge-2:5 MAC 172.0.0.11/16
participant 3 300 edge-3:5 MAC 172.0.0.21/16 edge-4:5 MAC 172.0.0.22/16

host AS ROUTER _ IP           # host names of form a1_100 a1_110

announce 1 100.0.0.0/24 110.0.0.0/24
announce 2 120.0.0.0/24 130.0.0.0/24
announce 3 140.0.0.0/24 150.0.0.0/24

flow a1 53 >> c
flow b1 53 >> c
flow c1 << 53
flow c1 1 | a1 ipv4_dst=140.0.0.1 udp_dst=53
flow c1 2 | a1 ipv4_dst=140.0.0.2 udp_dst=53
flow c1 3 | b1 ipv4_dst=140.0.0.1 udp_dst=53

listener AUTOGEN 8888
	
test init {
	listener
}

test regress {
	delay 10
	test start_all_send
	api 3 insert 0
	delay 76
	api 3 insert 1
	delay 20
	api 3 remove 5001
	api 3 insert 2
	api 3 remove 5002
	api 3 insert 3
	api 3 remove 5003
	api 3 insert 4
	api 3 remove 5004
	api 3 insert 5
	api 3 remove 5005
	api 3 insert 6
	api 3 remove 5006
	api 3 insert 7
	api 3 remove 5007
	api 3 insert 8
	api 3 remove 5008
	api 3 insert 9
	api 3 remove 5009
	api 3 insert 10
	api 3 remove 5010
	api 3 insert 11
	api 3 remove 5011
	api 3 insert 12
	api 3 remove 5012
	api 3 insert 13
	api 3 remove 5013
	api 3 insert 14
	api 3 remove 5014
	api 3 insert 15
	api 3 remove 5015
	api 3 insert 16
	api 3 remove 5016
	api 3 insert 17
	api 3 remove 5017
	api 3 insert 18
	api 3 remove 5018
	api 3 insert 19
	api 3 remove 5019
	api 3 insert 20
	api 3 remove 5020
	api 3 insert 21
	delay 1
	api 3 remove 5021
	api 3 insert 22
	delay 39
	api 3 remove 5022
	delay 113
	api 3 insert 23
	delay 111
	api 3 remove 5000
	api 3 insert 24
	api 3 remove 5024
	delay 1
	api 3 insert 25
	api 3 remove 5025
	delay 1
	api 3 insert 26
	delay 2
	api 3 remove 5026
	delay 263
	api 3 insert 27
	api 3 remove 5027
	api 3 insert 28
	api 3 remove 5028
	delay 130
	api 3 insert 29
	api 3 insert 30
	api 3 insert 31
	delay 69
	api 3 insert 32
	api 3 insert 33
	api 3 remove 5032
	api 3 remove 5033
	delay 108
	api 3 insert 34
	delay 15
	api 3 insert 35
	api 3 insert 36
	delay 351
	api 3 insert 37
	api 3 remove 5035
	delay 60
	api 3 insert 38
	delay 546
	api 3 insert 39
	api 3 remove 5039
	api 3 insert 40
	delay 10
	api 3 remove 5040
	api 3 insert 41
	api 3 remove 5041
	api 3 insert 42
	api 3 remove 5042
	api 3 insert 43
	test cycle_0
	test delay
	api 3 remove 5043
	api 3 insert 44
	api 3 remove 5044
	api 3 insert 45
	api 3 remove 5045
	api 3 insert 46
	api 3 remove 5046
	api 3 insert 47
	api 3 remove 5047
	api 3 insert 48
	api 3 remove 5048
	api 3 insert 49
	api 3 remove 5049
	api 3 insert 50
	api 3 remove 5050
	api 3 insert 51
	api 3 remove 5051
	api 3 insert 52
	api 3 remove 5052
	api 3 insert 53
	api 3 remove 5053
	api 3 insert 54
	api 3 remove 5054
	api 3 insert 55
	api 3 remove 5055
	api 3 insert 56
	api 3 remove 5056
	api 3 insert 57
	api 3 remove 5057
	api 3 insert 58
	api 3 remove 5058
	api 3 insert 59
	api 3 remove 5059
	api 3 insert 60
	api 3 remove 5060
	api 3 insert 61
	api 3 remove 5061
	api 3 insert 62
	api 3 remove 5062
	api 3 insert 63
	api 3 remove 5063
	api 3 insert 64
	delay 50
	api 3 remove 5064
	api 3 insert 65
	api 3 remove 5065
	api 3 insert 66
	api 3 remove 5066
	api 3 insert 67
	api 3 remove 5067
	api 3 insert 68
	api 3 remove 5068
	api 3 insert 69
	api 3 remove 5069
	api 3 insert 70
	api 3 remove 5070
	api 3 insert 71
	api 3 remove 5071
	api 3 insert 72
	api 3 remove 5072
	api 3 insert 73
	api 3 remove 5073
	api 3 insert 74
	api 3 remove 5074
	api 3 insert 75
	api 3 remove 5075
	api 3 insert 76
	api 3 remove 5076
	api 3 insert 77
	api 3 remove 5077
	api 3 insert 78
	api 3 remove 5078
	api 3 insert 79
	api 3 remove 5079
	api 3 insert 80
	api 3 remove 5080
	api 3 insert 81
	api 3 remove 5081
	api 3 insert 82
	api 3 remove 5082
	api 3 insert 83
	test cycle_1
	test delay
	api 3 remove 5083
	api 3 insert 84
	api 3 remove 5084
	api 3 insert 85
	api 3 remove 5085
	api 3 insert 86
	api 3 remove 5086
	delay 4
	api 3 insert 87
	api 3 remove 5087
	api 3 insert 88
	api 3 remove 5088
	delay 496
	api 3 insert 89
	api 3 remove 5089
	api 3 insert 90
	delay 60
	api 3 remove 5090
	api 3 insert 91
	api 3 remove 5091
	api 3 insert 92
	api 3 remove 5092
	api 3 insert 93
	api 3 remove 5093
	api 3 insert 94
	api 3 remove 5094
	api 3 insert 95
	api 3 remove 5095
	api 3 insert 96
	api 3 remove 5096
	api 3 insert 97
	api 3 remove 5097
	api 3 insert 98
	api 3 remove 5098
	api 3 insert 99
	api 3 remove 5099
	api 3 insert 100
	api 3 remove 5100
	api 3 insert 101
	api 3 remove 5101
	api 3 insert 102
	api 3 remove 5102
	api 3 insert 103
	api 3 remove 5103
	api 3 insert 104
	api 3 remove 5104
	api 3 insert 105
	api 3 remove 5105
	api 3 insert 106
	api 3 remove 5106
	api 3 insert 107
	api 3 remove 5107
	api 3 insert 108
	api 3 remove 5108
	api 3 insert 109
	api 3 remove 5109
	api 3 insert 110
	api 3 remove 5110
	delay 892
	api 3 remove 5036
	delay 32
	api 3 insert 111
	api 3 remove 5111
	api 3 insert 112
	api 3 remove 5112
	api 3 insert 113
	api 3 remove 5113
	api 3 insert 114
	api 3 remove 5114
	api 3 insert 115
	api 3 remove 5115
	api 3 insert 116
	api 3 remove 5116
	api 3 insert 117
	api 3 remove 5117
	api 3 insert 118
	api 3 remove 5118
	api 3 insert 119
	api 3 remove 5119
	api 3 insert 120
	api 3 remove 5120
	api 3 insert 121
	api 3 remove 5121
	api 3 insert 122
	api 3 remove 5122
	test cycle_2
	test delay
	api 3 insert 123
	api 3 remove 5123
	api 3 insert 124
	api 3 remove 5124
	api 3 insert 125
	api 3 remove 5125
	api 3 insert 126
	api 3 remove 5126
	delay 152
	api 3 insert 127
	delay 148
	api 3 insert 128
	api 3 remove 5128
	delay 8
	api 3 insert 129
	api 3 remove 5129
	delay 47
	api 3 insert 130
	delay 1180
	api 3 remove 5038
	api 3 insert 131
	api 3 remove 5131
	api 3 insert 132
	delay 990
	api 3 insert 133
	api 3 remove 5133
	delay 687
	api 3 insert 134
	delay 535
	api 3 remove 5127
	api 3 insert 135
	api 3 remove 5135
	api 3 insert 136
	api 3 remove 5136
	delay 123
	api 3 insert 137
	delay 215
	api 3 remove 5023
	api 3 insert 138
	api 3 remove 5138
	delay 4
	api 3 insert 139
	api 3 remove 5139
	delay 1164
	api 3 remove 5132
	delay 184
	api 3 insert 140
	delay 743
	api 3 insert 141
	api 3 remove 5141
	api 3 insert 142
	api 3 remove 5142
	api 3 insert 143
	api 3 remove 5143
	api 3 insert 144
	api 3 remove 5144
	api 3 insert 145
	api 3 remove 5145
	api 3 insert 146
	api 3 remove 5146
	api 3 insert 147
	api 3 remove 5147
	api 3 insert 148
	api 3 remove 5148
	api 3 insert 149
	api 3 remove 5149
	api 3 insert 150
	api 3 remove 5150
	api 3 insert 151
	api 3 remove 5151
	api 3 insert 152
	api 3 remove 5152
	api 3 insert 153
	api 3 remove 5153
	api 3 insert 154
	api 3 remove 5154
	api 3 insert 155
	api 3 remove 5155
	api 3 insert 156
	api 3 remove 5156
	api 3 insert 157
	api 3 remove 5157
	api 3 insert 158
	api 3 remove 5158
	api 3 insert 159
	api 3 remove 5159
	delay 119
	api 3 insert 160
	api 3 insert 161
	delay 437
	api 3 insert 162
	api 3 insert 163
	delay 125
	api 3 insert 164
	api 3 insert 165
	api 3 insert 166
	delay 50
	api 3 remove 5165
	test cycle_0
	test delay
	api 3 remove 5164
	api 3 remove 5166
	delay 178
	api 3 insert 167
	delay 302
	api 3 remove 5167
	delay 25
	api 3 insert 168
	api 3 remove 5168
	api 3 insert 169
	delay 50
	api 3 remove 5169
	api 3 insert 170
	delay 20
	api 3 remove 5170
	api 3 insert 171
	api 3 remove 5171
	api 3 insert 172
	api 3 remove 5172
	api 3 insert 173
	api 3 remove 5173
	api 3 insert 174
	api 3 remove 5174
	api 3 insert 175
	api 3 remove 5175
	api 3 insert 176
	api 3 remove 5176
	api 3 insert 177
	api 3 remove 5177
	api 3 insert 178
	api 3 remove 5178
	api 3 insert 179
	api 3 remove 5179
	api 3 insert 180
	api 3 remove 5180
	api 3 insert 181
	api 3 remove 5181
	api 3 insert 182
	api 3 remove 5182
	api 3 insert 183
	api 3 remove 5183
	api 3 insert 184
	api 3 remove 5184
	api 3 insert 185
	api 3 remove 5185
	api 3 insert 186
	api 3 remove 5186
	api 3 insert 187
	api 3 remove 5187
	api 3 insert 188
	api 3 remove 5188
	api 3 insert 189
	api 3 remove 5189
	api 3 insert 190
	api 3 remove 5190
	delay 3
	api 3 insert 191
	api 3 insert 192
	delay 6
	api 3 remove 5137
	api 3 insert 193
	api 3 remove 5193
	api 3 insert 194
	api 3 remove 5194
	delay 1
	api 3 insert 195
	api 3 remove 5195
	delay 43
	api 3 insert 196
	delay 86
	api 3 remove 5130
	api 3 insert 197
	api 3 remove 5197
	delay 85
	api 3 insert 198
	delay 432
	api 3 remove 5196
	api 3 insert 199
	api 3 remove 5199
	delay 528
	api 3 insert 200
	api 3 remove 5200
	api 3 insert 201
	api 3 remove 5201
	api 3 insert 202
	api 3 remove 5202
	api 3 insert 203
	api 3 remove 5203
	api 3 insert 204
	api 3 remove 5204
	api 3 insert 205
	api 3 remove 5205
	api 3 insert 206
	test cycle_1
	test delay
	api 3 remove 5206
	api 3 insert 207
	api 3 remove 5207
	api 3 insert 208
	api 3 remove 5208
	api 3 insert 209
	api 3 remove 5209
	api 3 insert 210
	api 3 remove 5210
	api 3 insert 211
	api 3 remove 5211
	delay 1
	api 3 insert 212
	api 3 remove 5212
	api 3 insert 213
	api 3 remove 5213
	api 3 insert 214
	api 3 remove 5214
	delay 361
	api 3 remove 5140
	delay 1
	api 3 insert 215
	api 3 remove 5215
	api 3 insert 216
	api 3 remove 5216
	delay 118
	api 3 insert 217
	delay 66
	api 3 insert 218
	delay 32
	api 3 insert 219
	delay 609
	api 3 remove 5217
	delay 4
	api 3 remove 5219
	api 3 insert 220
	api 3 remove 5220
	delay 151
	api 3 insert 221
	api 3 insert 222
	api 3 insert 223
	api 3 insert 224
	api 3 insert 225
	api 3 insert 226
	delay 466
	api 3 insert 227
	delay 1335
	api 3 insert 228
	api 3 insert 229
	api 3 insert 230
	api 3 insert 231
	api 3 insert 232
	api 3 insert 233
	api 3 insert 234
	api 3 insert 235
	api 3 insert 236
	api 3 insert 237
	api 3 insert 238
	api 3 insert 239
	api 3 insert 240
	api 3 insert 241
	api 3 insert 242
	api 3 insert 243
	api 3 insert 244
	api 3 insert 245
	api 3 insert 246
	api 3 insert 247
	api 3 insert 248
	api 3 insert 249
	api 3 insert 250
	api 3 insert 251
	api 3 insert 252
	api 3 insert 253
	api 3 insert 254
	api 3 insert 255
	api 3 insert 256
	api 3 insert 257
	api 3 insert 258
	api 3 insert 259
	api 3 insert 260
	api 3 insert 261
	api 3 insert 262
	api 3 insert 263
	api 3 insert 264
	api 3 insert 265
	api 3 insert 266
	api 3 insert 267
	api 3 insert 268
	api 3 insert 269
	api 3 insert 270
	api 3 insert 271
	test cycle_2
	test delay
	api 3 insert 272
	api 3 insert 273
	api 3 insert 274
	api 3 insert 275
	api 3 insert 276
	api 3 insert 277
	api 3 insert 278
	api 3 insert 279
	api 3 insert 280
	api 3 insert 281
	api 3 insert 282
	api 3 insert 283
	api 3 insert 284
	api 3 insert 285
	api 3 insert 286
	api 3 insert 287
	api 3 insert 288
	api 3 insert 289
	api 3 insert 290
	api 3 insert 291
	test stop_all_send
	delay 10
}

test xfer {
	verify a1_100 c1_140 8888
	verify b1_120 c1_140 8888
	verify a1_100 b1_120 8888
}

test show_table_2 {
    local ovs-ofctl dump-flows edge-1 -O OpenFlow13 table=3
    local ovs-ofctl dump-flows edge-2 -O OpenFlow13 table=3
}

test start_all_send {
    exec a1_100 iperf -c 140.0.0.1 -B 100.0.0.1 -p 53 -u -t 10000 -b 40M &IPERF_M1
    exec a1_100 iperf -c 140.0.0.2 -B 100.0.0.1 -p 53 -u -t 10000 -b 60M &IPERF_M2
    exec b1_120 iperf -c 140.0.0.1 -B 120.0.0.1 -p 53 -u -t 10000 -b 80M &IPERF_M3
}

test cycle_0 {
	delay 10
}

test cycle_1 {
	delay 10
}

test cycle_2 {
	delay 10
}

test delay {
	delay 15
	test show_table_2
	delay 15
}

test stop_all_send {
	killp a1_100 IPERF_M1
	killp b1_120 IPERF_M2
}

test info {
	local ovs-ofctl dump-flows edge-1 -O OpenFlow13
	exec a1 ip route
	exec b1 ip route
}

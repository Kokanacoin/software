import json
import datetime

data = '''{
 "StateCode": 1,
 "Reason": "成功",
 "Result": {
  "StartDate": "2020-10-09",
  "EndDate": "2020-11-07",
  "pc": "16994,18287,12019,17697,17706,18025,18042,16645,11614,11730,18692,17577,17226,17607,16437,11687,11243,19179,21807,21020,19757,18059,11848,11036,18498,18720,30578,22214,18464,12710",
  "mobile": "56205,60619,54847,53336,53818,55124,56898,55286,54882,53794,51338,51081,51288,51385,49601,52956,51385,52032,74519,73008,67925,61114,60770,56928,52806,55550,97643,74485,65163,61676"
 }
}'''

output_json = {}

data = json.loads(data)

StartDate = datetime.datetime.strptime(data['Result']['StartDate'], '%Y-%m-%d')
EndDate = datetime.datetime.strptime(data['Result']['EndDate'], '%Y-%m-%d')

ONEDAY = datetime.timedelta(days=1)

pc_data = data['Result']['pc'].split(',')
mobile_data = data['Result']['mobile'].split(',')

f = lambda i :{k:v for k,v in zip(['date','pc','mobile'],[(StartDate + i * ONEDAY).strftime('%Y-%m-%d'),pc_data[i],mobile_data[i]])}

output_json['status'] = data['StateCode']
output_json['data'] = [f(i) for i in range(len(pc_data))]

output_json = json.dumps(output_json, sort_keys=True, indent=4, separators=(',', ': '))

print(output_json)
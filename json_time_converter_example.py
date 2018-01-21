#!/usr/bin/env python3

import datetime
import re
import json

json_file = json.load(open('test.json'))
time_format = "%Y-%m-%d %H:%M:%S"
pattern = re.compile('2012-04-26.')

for data in json_file:
    json_file_time, ms = (data['updated']).split('.')
    datetime_object = datetime.datetime.strptime(json_file_time, time_format)
#get_timestamp = time.mktime(datetime.datetime.strptime(json_time, time_format).timetuple())
    final_time = datetime_object +  datetime.timedelta(hours=3)
    data['updated'] = final_time
    print(data.keys())
    if re.search(pattern, str(data['updated'])):
        print(data['id'], data['updated'])

from SQL import *
import json

# test data
data_str_0 = '{"project": "test1", "userName": "user1", "userTime": "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"}'
data_str_1 = '{"project": "test1", "userName": "user2", "userTime": "1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"}'
data_str_2 = '{"project": "test1", "userName": "user3", "userTime": "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"}'

data_json = [json.loads(data_str_0), json.loads(data_str_1), json.loads(data_str_2)]

s = SQL()
s.conn()

for i in range(0, 3):
    if(s.select(data_json[i]) == 0):
        s.insert(data_json[i])
    else:
        s.update(data_json[i])
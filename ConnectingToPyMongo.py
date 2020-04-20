import pymongo
import json
conn=pymongo.MongoClient()
db=conn['venkey']
print('db created')
print('client created')
with open('danny.json') as f:
    data=json.load(f)
    print(data['fruit'])

print(type(data))
jc=db['jsoncollection']
print('collection created')
jc.insert_one(data)
jc.find_one()


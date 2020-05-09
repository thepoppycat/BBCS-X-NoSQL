import pymongo
from pymongo import MongoClient
print("import successful")
cluster = MongoClient("mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority")
print("connected")
#mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority
db = cluster["finaltest"] #name of database is test
collection = db["test1"] #name of collection is test

pipeline = [
    {
    "$match": {"$and" :
        [{"age": {"$gte": 20, "$lt": 30}},
        {"company": {"$in": ["PRINTSPAN", "TECHMANIA", "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
        {"eyeColor": {"$nin": ["black", "brown"]}},
        {"friends.name": {"$regex": "^C"}}
    ]}},
    {"$project": {"name": 1, "_id": 0}}
]

result = collection.aggregate(pipeline)
for i in result:
    print (i)

print("is this working?")
print("ending")

#https://www.gitpod.io/blog/gitpodify/
#https://www.gitpod.io/docs/getting-started/
#https://www.gitpod.io/docs/git/

#killer is 62

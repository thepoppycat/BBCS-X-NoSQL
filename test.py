'''
import pymongo
from pymongo import MongoClient
print("import successful")
cluster = MongoClient("mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority")
print("connected")
#mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority
db = cluster["test"] #name of database is test
collection = db["test"] #name of collection is test

post = {"_id": 10, "name": "yx", "score": 100}
#print(post)

post1 = {"_id": 1, "name": "yx", "score": 100}
post2 = {"_id": 2, "name": "yx", "score": 100}
#post3 = {"name": "joel", "score": 1000}
#collection.insert_one(post3)
#collection.insert_many([post1, post2])

results = collection.find({"name": {"$regex": "^j"}})

results1 = collection.find_one({"name": "yx"})

print(results1)

for result in results:
    print(result)

results_del = collection.delete_one({"_id": 0}) #delete
results_del_many = collection.delete_many({"name": "joel"}) #delete

results_update = collection.update_one({"_id": 10}, {"$set": {"name": "joelleo"}}) #updates one entry that has the id of 10 and set the name data to joelleo
'''

'''
pipeline = [
    {"$match": {"name": "yx"}}
]
'''

#--------------------------------------------------------------------------------------------------------------
#main
import pymongo
from pymongo import MongoClient
print("import successful")
cluster = MongoClient("mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority")
print("connected")
#mongodb+srv://test1:test1@cluster0-d9jjq.mongodb.net/test?retryWrites=true&w=majority
db = cluster["test1"] #name of database is test
collection = db["test1"] #name of collection is test

collection.delete_many({})
'''
post = [
    {"cust_id": "A123", "amount": 500, "status": "A"},
    {"cust_id": "A123", "amount": 250, "status": "A"},
    {"cust_id": "B121", "amount": 200, "status": "A"},
    {"cust_id": "A123", "amount": 300, "status": "B"}
]
collection.insert_many(post)
'''

'''
pipeline = [
    {"$match": {"status": "A"}},
    {"$group": {
        "_id": "$cust_id",
        "total": {"$sum": "$amount"}
    }}
]

result = collection.aggregate(pipeline)

final_ans = {}
distinct_cust_id = collection.distinct("cust_id")

for i in distinct_cust_id:
    result = collection.find(
        filter = {"status": "A", "cust_id": i},
        projection = {"_id": 0, "cust_id": 1, "amount": 1}
    )
    total = 0
    for j in result:
        total += j["amount"]
        final_ans[j["cust_id"]] = total

print(final_ans)

print("ending")'''

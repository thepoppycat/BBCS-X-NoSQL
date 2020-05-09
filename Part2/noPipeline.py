import _____
from _____ import ______
uri = "_________________________________" #add in your MongoDB connection string here
cluster = MongoClient(uri)

db = cluster["__________"] #insert name of database you created earlier here
collection = db["__________"] #insert name of collection you created earlier here

result = collection.___(
            _____ = {"$and" : [
                {"age": {"$gte": 20, "$lt": 30}},
                {"company": {"$in": ["PRINTSPAN", "TECHMANIA", "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
                {"eyeColor": {"$nin": ["black", "brown"]}},
                {"friends.name": {"$regex": "^C"}}
            ]},
            _____ = {
                "____": ____,
                "____": ____
            }
        )

#Note: collection.find() returns you a cursor object so need to iterate through result to get the actual values.
for i in result:
    print (i)

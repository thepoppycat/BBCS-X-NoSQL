import _____
from _____ import ______
uri = "_________________________________" #add in your MongoDB connection string here
cluster = MongoClient(uri)

db = cluster["__________"] #insert name of database you created earlier here
collection = db["__________"] #insert name of collection you created earlier here

pipeline = [
    {"$___": {"$___" : [
        {"______": {"$___": 20, "__": 30}},
        {"______": {"$___": ["PRINTSPAN", "TECHMANIA", "NEPTIDE", "MULTRON", "SKYNET", "UPDAT", "STANTON"]}},
        {"______": {"$___": ["black", "brown"]}},
        {"______": {"$___": "^C"}}
    ]}},
    {"$____":
        {"______": 1, "______": 0}}
]

#time to use the pipeline!
#Note: pipeline aggregation returns you a cursor object to the MongoDB database so you need to iterate through result to get the actual values.
result = collection.______(pipeline)
for i in result:
    print (i)

# Pipeline Aggregation for MongoDB with pymongo

For this workshop, we shall be going through reading the database using the `.aggregate()` method on a database collection and finding out who stole the sacred BuildingBloCS Logo. [Click here to see the storyline](https://github.com/joelleoqiyi/BBCS-X-NoSQL/tree/master/Part1)

Before we go through how to use pipeline aggregation with NoSQL, we need to import our possible suspects (in names.json)

---

1) In MongoDB Atlas, click on your cluster name and then click `Command Line Tools`. You should see something like this:

![](../images/MongoDBAtlas_CommandLineTools.png)

2) Scroll down till `Data Import and Export Tools` and copy the command line code for `mongoimport` (we are **importing** data using the `mongoimport` function)

It should look something like this:
```
mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-d8ikq.mongodb.net:27017,cluster0-shard-00-01-d8ikq.mongodb.net:27017,cluster0-shard-00-02-d8ikq.mongodb.net:27017 --ssl --username <USERNAME> --password <PASSWORD> --authenticationDatabase admin --db <DATABASE> --collection <COLLECTION> --type <FILETYPE> --file <FILENAME>
```
3) In Gitpod, paste and run the command line code (which you copied) into the terminal, replace the following things:
- `<USERNAME>` with your MongoDB user's username (not the one to your account)
- `<PASSWORD>` with your MongoDB user's password (not the one to your account)
- `<DATABASE>` with the name of your database (if enter a name that currently exist in your MongoDB cluster, MongoDB would create a new database for you)
- `<COLLECTION>` with the name of your collection (if enter a name that currently exist in your MongoDB cluster, MongoDB would create a new collection for you)
- `<FILETYPE>` with the type of the file that you are going to import (in our case type `json`)
- `<FILENAME>` with the name of the file you are going to import (in our case `names.json`)

You also need to add in `--jsonArray`, this tells MongoDB that your json file is already formatted properly.

It should look something like this:
```
mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-d8ikq.mongodb.net:27017,cluster0-shard-00-01-d8ikq.mongodb.net:27017,cluster0-shard-00-02-d8ikq.mongodb.net:27017 --ssl --username sampleusername --password samplepassword --authenticationDatabase admin --db suspectsDatabase --collection suspectsCollections --type json --file names.json --jsonArray
```


---

Next we need to connect to the cluster --> database --> collection
```
import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient(<MongoDB server here>)

db = cluster["<database name here>"] #insert name of database you created earlier here
collection = db["<collections name here>"] #insert name of collection you created earlier here
```
If you're running your MongoDB server locally, then by default your local MongoDB IP address and port is `'127.0.0.1', 27017` respectfully. If you wanna connect to the MongoDB Atlas as explained in the workshop then please follow the instructions in the README.MD in the root of this repository.

---

Previously, you learnt the basics of pymongo such as `db.collections.find()` to find/read from MongoDB Atlas.

#### But what is pipeline aggregation?

The MongoDB aggregation pipeline consists of **stages**. Each stage transforms the documents as they pass through the pipeline. Pipeline stages do not need to produce one output document for every input document; e.g., some stages may generate new documents or filter out documents.

Pipeline stages can appear multiple times in the pipeline with the exception of `$out`, `$merge`, and `$geoNear` stages. For a list of all available stages, see [Aggregation Pipeline Stages](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/#aggregation-pipeline-operator-reference). This makes certain tasks easier as you would not have to deal with needing to use `db.collections.find()` or other query methods multiple times, you would also not as likely need to do pre/post-processing of data using python as you are able to "compile" all the different tasks you need to do (before your final output) into a **pipeline** and aggregate them all at once, **making complex tasks significantly easier to understand and execute**.

MongoDB provides the `db.collection.aggregate()` method in the mongo shell to run the aggregation pipeline.

Lets look at an example:

The following code uses pipeline aggregation.
```
pipeline = [
  {"$match": {"status": "A"}},
  {"$group": {
    "_id": "$cust_id",
    "total": {"$sum": "$amount"}
  }}
]

result = db.collection.aggregate(pipeline)
```
while the following code does not:
```
final_ans = {}
distinct_cust_id = db.collection.distinct("cust_id")

for i in distinct_cust_id:
    result = db.collection.find(
        filter = {"status": "A", "cust_id": i},
        projection = {"_id": 0, "cust_id": 1, "amount": 1}
    )
    total = 0
    for j in result:
        total += j["amount"]
        final_ans[j]["cust_id"]] = total

print(final_ans)
```
We won't be going through `db.collection.distinct()` and `$group (aggregation)`, you can view a short video about the code above through [this link](https://docs.mongodb.com/manual/_images/agg-pipeline.mp4), but some things to consider is that, although both codes does and outputs the same dictionary, pipeline aggregation does it in a **more succinct and concise way** compared to the one which doesn't.

---

Here is some "conversion" between pipeline aggregation and normal query:

|Normal Query| Pipeline Aggregation stages|
|--|--|
|db.collections.find(\<query>)  |{ [$match](https://docs.mongodb.com/manual/reference/operator/aggregation/match/): { \<query> } }  |
|db.collections.find(\<projection>)| { [$project](https://docs.mongodb.com/manual/reference/operator/aggregation/project/): { \<specification(s)> } }|
|db.collection.distinct(\<query>) + pre/post-processing in python | { [$group](https://docs.mongodb.com/manual/reference/operator/aggregation/group/): { _id: \<expression>, \<field1>: { \<accumulator1> : \<expression1> }, ...}}|
|db.collections.find().limit(\<positive integer>) | { [$limit](https://docs.mongodb.com/manual/reference/operator/aggregation/limit/): \<positive integer> }|
|db.collection.countDocuments( \<query>, \<options> ) | { [$count](https://docs.mongodb.com/manual/reference/operator/aggregation/count/): \<string> } |
| ... | ... |



##

And here concludes the end of our MongoDB tutorial Part 2! :). For any questions, feel free to ask us on Discord

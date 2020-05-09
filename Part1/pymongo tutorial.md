#Fundamental C.R.U.D functions of persistent storage

C - Create
R - Read
U - Update
D - Delete

Before we go through the CRUD details, we shall connect to a client/cluster first
'''
import pymongo

client = pymongo.MongoClient(<MongoDB server here>)

'''
For this ~~cheatsheet~~ example, our database will be consumables, collection be food, and documents be banana.
### Create

In MongoDB, creating a database/collection has the same function as routing to it.

..* **Creating/Connecting to a database within a client**
'''
Consumables_database = client.get_database('Consumables') 
'''
In the above code snippet, `Consumable_database` is merely a variable placeholder in the pymongo command line... You can call it whatever you want as long as it's easy to understand. For me I follow the convention <databasename>_database so that it's easier to understand.
  
  As for `client.get_database('Consumables')`, Consumables is the name of the database you want to create/connect to.
  
  ..* **Creating/Connecting to a collection within a database**
  ```
  Fruits_collection = Consumables_database.get_collection('Fruits')
  ```
  The naming convention follows similarly for the earlier snippet, nothing much to explain here.
  Remember I am only creating one collection for this example, you can create as many collections as you want within a database. So lets say you wanna make a drinks collection just do `Drinks_collection = Consumables_database.get_collection('Drinks')`
  
  ..* **Adding documents into a collection**
  To insert documents into a collection, we use the following function:
  ```
  Fruits_collection.insert_one(data)
  ```
  benis gay

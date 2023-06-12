from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

# client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

db = client.neuraldb

people = db.people

mike_id = people.insert_one({"name": "Paul", "age": 32}).inserted_id
people.insert_one({"name": "Lisa", "age": 20, "interests": ["C++", "Java"]})
people.insert_one({"name": "Paul", "age": 40})
people.insert_one({"name": "Paul", "age": 27})
people.insert_one({"name": "Lisa", "age": 26, "interests": ["C++", "Java"]})
people.insert_one({"name": "John", "age": 78})

for person in people.find():
    print(person)

print(mike_id)

print([p for p in people.find({"name": "Paul"})])

print([p for p in people.find({"_id": ObjectId("648727e02e32f3fb6e14eea7")})])

print([p for p in people.find({"age": {"$lt": 21}})])

print(people.count_documents({"name": "Lisa"}))

people.update_one({"_id": ObjectId("648726703db569dba9cb12ed")}, {"$set": {"age": 27}})

# people.delete_many({"age": {"$lt": 37}})

pipeline = [
    {
        "$group": {
            "_id": "$name",
            "averageAge": {"$avg": "$age"}
        }
    },
    {
        "$sort": SON([("averageAge", -1), ("_id", -1)])
    }
]

results = people.aggregate(pipeline)
for result in results:
    print(result)

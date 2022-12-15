from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.admin
collection = db["film"]

# cursor = collection.find()
# for record in cursor:
#     print(record)
res = db.film.find().limit(2)
data = []
for i in res:
    pass

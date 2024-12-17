import pymongo

# Establish a client connection
# client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")

# Get MongoDB server version
# client.list_database_names() # ['admin', 'config', 'local']

# Close the client connection
# client.close()

# client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
client = pymongo.MongoClient("mongodb://admin:admin@mongo:27017/")

db = client["test"]
print(client.list_database_names()) # "test" is not created until you add content

collection = db["example"]
name = { "name": "Ashley" }
x = collection.insert_one(name)

print(x.inserted_id) # 67530cd7f6cce3bb6abb86ba
print(client.list_database_names()) # ['admin', 'config', 'local', 'test']

names = [
    { "name": "Barry"},
    { "name": "Christina"}
]
x = collection.insert_many(names)

for i in x.inserted_ids:
    print(i)
# 67530e71f6cce3bb6abb86bb, 67530e71f6cce3bb6abb86bc

collection.find_one({ "name": "Ashley" }) # {'_id': ObjectId('67530cd7f6cce3bb6abb86ba'), 'name': 'Ashley'}

# Close the connection
client.close()

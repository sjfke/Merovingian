import valkey

# connection = valkey.Valkey(host='localhost', port=6379, db=0)
# connection.ping()         # True
# connection.client_info()  # Client Information as a dictionary
# connection.close()        # Does nothing


connection = valkey.Valkey(host='localhost', port=6379, db=0)
connection.delete("names")  # ensure 'names' is empty
connection.lpush("names", "Ashley")
connection.rpush("names", "Barry", "Christina")

# print(connection.lindex("names", 0))
print(connection.lindex("names", 0).decode("utf-8"))



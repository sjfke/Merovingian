import valkey

# connection = valkey.Valkey(host='localhost', port=6379, db=0)
# connection.ping()         # True
# connection.client_info()  # Client Information as a dictionary
# connection.close()        # Does nothing

connection = valkey.Valkey(host='localhost', port=6379, db=0)

# List
connection.delete("names")
connection.lpush("names", "Ashley")                 # 1, new length
connection.rpush("names", "Barry", "Christina")     # 3, new length
connection.lrange("names", 0, -1)                     # [b'Ashley', b'Barry', b'Christina']
connection.lindex("names", 0)                        # b'Ashley' (bytes)
print(connection.lindex("names", 0).decode("utf-8")) # Ashley (str)
connection.lpop("names")                                         # b'Ashley' (bytes)
connection.lrange("names", 0, -1)                     # [b'Barry', b'Christina']
connection.rpop("names")                                         # b'Christina'
connection.lrange("names", 0, -1)                     # [b'Barry']
connection.delete("names")                                       # 1 Successful
connection.llen("names")                                         # 0, new length

# Hash
connection.delete("names")
connection.hset("names", "Ashley", 1)   # 1
connection.hset("names", "Barry", 2)    # 1
connection.hset("names", "Cristina", 3) # 1
connection.hgetall("names")                              # {b'Ashley': b'1', b'Barry': b'2', b'Cristina': b'3'}
connection.hexists("names", "Ashley")         # True
connection.hexists("names", "Barley")         # False
# connection.close()                                    # Does nothing

exit()
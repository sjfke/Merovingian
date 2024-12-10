import valkey

# connection = valkey.Valkey(host='localhost', port=6379, db=0)
# connection.ping()         # True
# connection.client_info()  # Client Information as a dictionary
# connection.close()        # Does nothing

connection = valkey.Valkey(host='localhost', port=6379, db=0, decode_responses=True)

# List
connection.delete("names")
connection.lpush("names", "Ashley")                 # 1, new length
connection.rpush("names", "Barry", "Christina")     # 3, new length
connection.lrange("names", 0, -1)                     # ['Ashley', 'Barry', 'Christina']
connection.lindex("names", 0)                        # 'Ashley'
connection.lpop("names")                                         # 'Ashley'
connection.lrange("names", 0, -1)                     # ['Barry', 'Christina']
connection.rpop("names")                                         # 'Christina'
connection.lrange("names", 0, -1)                     # ['Barry']
connection.delete("names")                                       # 1 Successful
connection.llen("names")                                         # 0, new length

# Hash
connection.delete("names")
connection.hset("names", "Ashley", 1)   # 1
connection.hset("names", "Barry", 2)    # 1
connection.hset("names", "Cristina", 3) # 1
connection.hgetall("names")                              # {'Ashley': '1', 'Barry': '2', 'Cristina': '3'}
connection.hexists("names", "Ashley")         # True
connection.hexists("names", "Barley")         # False
# connection.close()                                    # Does nothing

exit()
import valkey

connection = valkey.Valkey(host='localhost', port=6379, db=0)
connection.ping()


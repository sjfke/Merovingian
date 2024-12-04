from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://user:password@localhost:3306/test?charset=utf8mb4")

# Establish a connection
# connection = engine.connect()
# Close the connection
# connection.close()

with engine.connect() as connection:
    connection.execute(text("CREATE TABLE example (id INTEGER, name VARCHAR(20))"))
    connection.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
    connection.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
    connection.commit()

    result = connection.execute(text("SELECT * FROM example WHERE name = :name"), dict(name="Ashley"))

    for row in result.mappings():
        print("Author:", row["name"])
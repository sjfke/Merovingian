# Import SQLAlchemy's create_engine function
from sqlalchemy import create_engine, text

# Create a connection string
# [Python postgres drivers](https://wiki.postgresql.org/wiki/Python)
# most popular 'psycopg2' pip install fails with MS Windows Python
# engine = create_engine("postgresql+psycopg2://admin:admin@localhost:5432/test")
# engine = create_engine("postgresql+pg8000://admin:admin@localhost:5432/test")
engine = create_engine("postgresql+pg8000://admin:admin@postgres:5432/test")

# Test the connection
# connection = engine.connect()
# print("Connected to PostgreSQL database successfully!")
# connection.close()

with engine.connect() as connection:
    connection.execute(text("CREATE TABLE example (id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL)"))
    connection.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
    connection.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
    connection.commit()

    result = connection.execute(text("SELECT * FROM example WHERE name = :name"), dict(name="Ashley"))

    for row in result.mappings():
        print("Author:", row["name"])
from sqlalchemy import create_engine

# Define the PostgreSQL URL
postgresql_url = 'postgresql://admin:admin@localhost:5432/test'

# Create an engine
engine = create_engine(postgresql_url)

# Establish a connection
connection = engine.connect()

# Close the connection
connection.close()
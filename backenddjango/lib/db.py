from psycopg_pool import ConnectionPool
import os

connection_url = os.getenv("CONNECTION_URL")
print("##############################################")
print(connection_url)
print("##############################################")
pool = ConnectionPool (connection_url)
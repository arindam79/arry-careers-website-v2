import os
import psycopg2

# Create an engine to connect to the database

DATABASE_URL = "postgresql://arindam:wxaCNMrEszm5_RNBDLazpA@meaty-faun-5842.6xw.cockroachlabs.cloud:26257/arrycareers?sslmode=verify-full"

conn = psycopg2.connect(os.environ[DATABASE_URL])
# Create a cursor object to execute SQL queries
with conn.cursor() as cur:
  cur.execute("SELECT now()")
  res = cur.fetchall()
  conn.commit()
  print(res)

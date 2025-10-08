from datetime import datetime, timedelta, timezone
from .db import query_wrap_array
from .db import pool

import boto3
from psycopg_pool import ConnectionPool
import os

class HomeActivities:
  def run(self):
    print("|||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||")
    print(os.getenv("CONNECTION_URL"))
    sql =query_wrap_array("""
    SELECT * FROM activities
    """)
##
    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        json = cur.fetchall()
        print(json)
    return json[0]
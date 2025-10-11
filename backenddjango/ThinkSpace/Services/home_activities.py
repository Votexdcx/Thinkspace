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
    #print(os.getenv("CONNECTION_URL"))
    sql =query_wrap_array("""
       SELECT 
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
    FROM public.activities
    LEFT JOIN public.users ON users.uuid = activities.user_uuid
    ORDER BY activities.created_at DESC

    """)
##
    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        json = cur.fetchone()
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print(json[0])

    return json[0]
#!/usr/bin/env python3
from datetime import datetime,timedelta,timezone
import boto3
import sys
from psycopg_pool import ConnectionPool
from db import query_wrap_array
from db import pool
from boto3 import client


def create_message(client, message, my_user_uuid, my_user_display_name, my_user_handle,created_at, message_group_uuid):
    pass

attrs = {
    'endpoint_ur1': 'http://localhost: 8001'
}
# unset endpoint url for use with production database
#if len(sys.argv) == 2:
#    if "prod" in sys.argv[1]:
#        attrs = {}
#dynamodb = boto3.client( 'dynamodb',**attrs)

sql=query_wrap_array("""
       SELECT users.uuid, users.display_name, users.handle from users 
       WHERE display_name IN ('Andrew Brown', 'Andrew Bayko')
    """)
with pool.connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        json = cur.fetchone()
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print("kqwhdkahdskjhdkajshdkjahskjdhksahdkh")
        print(json[0])


Conversation = """
PersonA: I told you we were supposed to leave at 6, not 6:30!
PersonB: I know, but the traffic was terrible and I couldn’t help it.
PersonA: You could’ve at least called! We missed the first part of the movie.
PersonB: It’s not the end of the world. We can still enjoy what’s left.
PersonA: That’s not the point — it’s about being on time! You always do this.
PersonB: Always? Really? That’s not fair. Last weekend I was the one waiting for you.
PersonA: That was different. I was finishing work, not just “running late.”
PersonB: And today I was finishing errands for both of us! You asked me to pick up snacks, remember?
PersonA: Yes, but I didn’t think it would take you half an hour to grab chips and soda.
PersonB: You didn’t see the line. It was chaos in there. Everyone’s doing last-minute shopping.
PersonA: You could’ve told me! I was sitting here getting more and more frustrated.
PersonB: I tried texting, but my phone died halfway through. I even asked the cashier if they had a charger.
PersonA: Fine, but this keeps happening. You don’t plan ahead.
PersonB: Maybe because you over-plan everything. It’s exhausting trying to keep up with your schedule.
PersonA: So now it’s my fault for wanting to be organized?
PersonB: No, it’s just... sometimes it feels like you care more about the schedule than the moment.
PersonA: That’s not true. I just want things to go smoothly.
PersonB: Then maybe next time, we both try to meet in the middle — I’ll plan better, and you relax a little.
PersonA: (sighs) Maybe you’re right. I just hate being late.
PersonB: I know. And I hate seeing you stressed. Truce?
PersonA: Truce. But next time, we’re leaving at 5:45.
PersonB: Deal — as long as you promise not to set ten reminders on my phone again.
PersonA: No promises.
"""
now = datetime.now(timezone.utc).astimezone()
lines = Conversation.lstrip('\n').rstrip('\n').split('\n')
i = 0
for line in lines:
    i +=1
    if line.startswith("PersonA"):
        key = 'my_user'
        message = line.replace('PersonA: ','')
    elif line.startswith("PersonB"):
        key = 'other_user'
        message = line.replace('PersonB: ', '')
    else:
        print(line)
        raise 'Invalid line'
    created_at = (now +timedelta(minutes=i))
    #.create_message(client=ddb, message= message,my_user_uuid = users[key]['uuid'] ,my_user_display_name = users[key]['display_name'] ,my_user_handle =users[key]['handle'] ,created_at = created_at, message_group_uuid=message_group_uuid)

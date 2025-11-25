#!/usr/bin/env python3
from datetime import datetime,timedelta,timezone
import sys
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool
from db import query_wrap_array
from db import pool
from boto3 import client
import boto3
import uuid


def create_message(client, message, my_user_uuid, my_user_display_name, my_user_handle,created_at, message_group_uuid):
    print("Createmessage/////")
    record = {
        'PartitionKey': {'S': f"MSG#{message_group_uuid}"},
        'SecondaryKey': {'S': created_at},
        'message_uuid': {'S': str(uuid.uuid4())},
        'message': {'S': message},
        'user_uuid': {'S':str(my_user_uuid)},
        'user_display_name': {'S': my_user_display_name},
        'user_handle': {'S': my_user_handle}
    }
    print("RECORD")
    print(record)
    response = dynamodb.put_item(
        TableName='ThinkspaceMessage',
        Item=record)



attrs = {
    'aws_access_key_id':'dummy',
    'aws_secret_access_key':'dummy',
    'region_name':'us-east-1',
    'endpoint_url':'http://localhost:8001'
}
# unset endpoint url for use with production database
if len(sys.argv) == 2:
    if "prod" in sys.argv[1]:
        attrs = {'region_name': 'eu-west-1'}
        print("//////////////////////////////7")
        print("prod")
dynamodb = boto3.client( 'dynamodb',**attrs)

def create_message_group(dynamodb, message_group_uuid, my_user_uuid,other_user_uuid, other_user_display_name,other_user_handle, last_message_at=None,message=None):
    table_name = 'ThinkspaceMessage'
    last_message_at = last_message_at or "NONE"
    message = message or ""
    record = {
        'PartitionKey': {'S': f"GRP#{my_user_uuid}"},
        'SecondaryKey': {'S': last_message_at},
        'message_group_uuid': {'S': message_group_uuid},
        'message': {'S': message},
        'user_uuid': {'S': other_user_uuid},
        'user_display_name': {'S': other_user_display_name},
        'user_handle': {'S': other_user_handle}  # fixed key
    }
    print(record)
    response = dynamodb.put_item(
        TableName ='ThinkspaceMessage',
        Item = record)


def usersuuid():
    sql=("""
           SELECT users.uuid, users.display_name, users.handle from users 
           WHERE display_name IN ('Andrew Brown', 'Andrew Bayko')
        """)
    with pool.connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(sql)
            users = cur.fetchall()
            my_user = next(item for item in users if item["handle"] == 'andrewbrown')

            other_user = next((item for item in users if item["handle"] == 'bayko'), None)
            results = { 'my_user': my_user,
                'other_user': other_user,
                }
            return  results

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

users = usersuuid()
my_user = users['my_user']
other_user = users['other_user']

message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
now = datetime.now(timezone.utc).astimezone()
#print(users['my_user'])
create_message_group(
    dynamodb,
    message_group_uuid,
    str(my_user['uuid']),
    str(other_user['uuid']),
    other_user['display_name'],
    other_user['handle'],
    "lastmessage123",   # last_message_at
    "message"   # message
)
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
    created_at = (now +timedelta(minutes=i)).isoformat()
    create_message(client=dynamodb, message= message,my_user_uuid = users[key]['uuid'] ,my_user_display_name = users[key]['display_name'] ,my_user_handle =users[key]['handle'] ,created_at = created_at, message_group_uuid=message_group_uuid)
    #create_message(client =dynamodb,message="this is a filler message",my_user_uuid=users['other_user']['uuid'], other_user_display_name=users['my_user']['display_name'],other_user_uuid=users['my_user']['uuid'],other_user_handle=users['my_user']['handle'],Last_message_at = now.isoformat(),message_group_uuid = message_group_uuid)
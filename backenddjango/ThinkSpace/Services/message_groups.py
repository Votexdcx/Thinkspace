from datetime import datetime, timedelta, timezone
from psycopg_pool import ConnectionPool
import boto3

class MessageGroups:
  def run(self,user_handle):
    model = {
      'errors': None,
      'data': None
    }
    
    
    
    user_uuid =CreateQuery(self, user_handle)
    attrs = {
    'aws_access_key_id':'dummy',
    'aws_secret_access_key':'dummy',
    'region_name':'us-east-1',
    'endpoint_url':'http://dynamodb-local:8000'
    }
    dynamodb = boto3.client( 'dynamodb',**attrs)
    message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
    #queryparams = {
    #  'TableName': 'ThinkspaceMessage',
    #  'KeyConditionExpression': 'PartitionKey = :PartitionKey',
    #  'ScanIndexForward': False,
    #  'Limit': 20,
    #  'ExpressionAttributeValues':{
    #    ':PartitionKey': {'S': f"MSG#{message_group_uuid}"}
    #  },
    #  'ReturnConsumedCapacity': 'TOTAL'
    #}
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    #print(user_uuid)
    #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    queryparams = {
      'TableName': 'ThinkspaceMessage',
      'ScanIndexForward': False,
      'KeyConditionExpression': 'PartitionKey = :PartitionKey',
      'ExpressionAttributeValues':{
        ':PartitionKey': {'S': f"GRP#{'0faf4884-222e-40b4-ba68-e358264ce431'}"}
      },
      'ReturnConsumedCapacity': 'TOTAL'
    }
  
    response =dynamodb.query(**queryparams)
    print()
    print("response:", response)
    model['data'] = response
    return model
  
  
def CreateQuery(self,cognito_user_id):
    
    
    connection_url = "postgresql://Thinkspacedb:quwrem-firjyz-vipmA7@thinkspace.c32ye0guaums.eu-west-2.rds.amazonaws.com:5432/thinkspace"
    pool = ConnectionPool(conninfo=connection_url)
    sql = f"""
      SELECT users.uuid FROM public.users 
      WHERE   cognito_user_id = %(cognito_user_id)s
      LIMIT 1
      """
    
    with pool.connection() as conn:
      with conn.cursor() as cur:
        parameters = {
          "cognito_user_id":cognito_user_id,
        }
        uuid = cur.execute(sql, parameters)
        conn.commit()
        json = cur.fetchone()
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(json[0])
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        return json[0]
import uuid
from datetime import datetime, timedelta, timezone
from .db import query_wrap_array
from .db import pool
class CreateActivity:
  def run(self, message,ttl,user_handle ):
    model = {
      'errors': None,
      'data': None
    }
    print("////////////////////////////////////////")
    print("message:", message)
    print("userhandle:", user_handle)
    print("time;", ttl)
    now = datetime.now(timezone.utc).astimezone()

    if (ttl == '30-days'):
      ttl_offset = timedelta(days=30) 
    elif (ttl == '7-days'):
      ttl_offset = timedelta(days=7) 
    elif (ttl == '3-days'):
      ttl_offset = timedelta(days=3) 
    elif (ttl == '1-day'):
      ttl_offset = timedelta(days=1) 
    elif (ttl == '12-hours'):
      ttl_offset = timedelta(hours=12) 
    elif (ttl == '3-hours'):
      ttl_offset = timedelta(hours=3) 
    elif (ttl == '1-hour'):
      ttl_offset = timedelta(hours=1) 
    else:
      model['errors'] = ['ttl_blank']

    if user_handle == None:
      model['errors'] = ['user_handle_blank']

    if message == None or len(message) < 1:
      model['errors'] = ['message_blank'] 
    elif len(message) > 280:
      model['errors'] = ['message_exceed_max_chars'] 


    ttl_offset2 = (now + ttl_offset).isoformat()
    print(ttl_offset2)
    if model['errors']:
      model['data'] = {
        'handle':  uuid,
        'message': message
      }   
    else:
        self.CreateQuery(message,ttl_offset2, user_handle)
        model['data'] = {
        'uuid': uuid.uuid4(),
        'display_name': 'Andrew Brown',
        'handle':  user_handle,
        'message': message,
        'created_at': now.isoformat(),
        'expires_at': (now + ttl_offset).isoformat()
      }
    return model
  
  def CreateQuery(self, message, ttl, user_handle):
     
    sql = f"""
        INSERT INTO public.activities( 
          user_uuid,
          message,
          expires_at
        )
        VALUES 
        (
         (SELECT uuid FROM public.users WHERE users.handle = %(user_handle)s LIMIT 1),
         %(message)s,
         %(ttl)s
        )RETURNING uuid;
      """
    
    with pool.connection() as conn:
      with conn.cursor() as cur:
        parameters = {
          "user_handle":user_handle,
          "message": message,
          "ttl":ttl
        }
        cur.execute(sql, parameters)
        conn.commit()
        json = cur.fetchone()
        print(json[0])


    
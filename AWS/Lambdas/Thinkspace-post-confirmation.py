import json
import os
import pg8000
import email

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print("akdfhkdashfjksdhfkjshfkjsdhfkjshdfkjhdskjfhskjdhfkjsdhfkjhsdkj")
    print(user)
    try:
        conn = pg8000.connect(
            user="Thinkspacedb",
            password="quwrem-firjyz-vipmA7",
            host="thinkspace.c32ye0guaums.eu-west-2.rds.amazonaws.com",
            port=5432,
            database="thinkspace"
        )

        cur = conn.cursor()
        user_display_name = user['preferred_username']
        user_email = user['email']
        user_handle = user['given_name']
        user_cognito_id = user['sub']
        print(user_display_name)
        print(user_email)
        print(user_handle)
        print(user_cognito_id)
        sql = f"""
            INSERT INTO users( 
             display_name,
             email,
             handle,
             cognito_user_id
            )
            VALUES 
            (
            '{user_display_name}',
            '{user_email}',
            '{user_handle}',
            '{user_cognito_id}'
            )
         """
        cur.execute(sql)
        conn.commit()
    except (Exception, pg8000.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('PostgreSQL connection is closed')
    return event

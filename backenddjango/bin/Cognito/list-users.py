#!/usr/bin/env python3
import boto3
import os
import json


user_poolID = "eu-west-2_uhta1UGB8"

client = boto3.client("cognito-idp")

params = {
    'UserPoolId': user_poolID,
    'AttributesToGet':[
        'preferred_username',
        'sub'
    ]
}
response = client.list_users(**params)
users = response['Users']
#print (json. dumps (users, sort_keys=True, indent=2, default=str))
dict_users = {

}
for user in users:
    #print (json. dumps (user, sort_keys=True, indent=2, default=str))
    sub = next(attr["Value"] for attr in user["Attributes"] if attr["Name"] == "sub"),None
    handle = next(attr["Value"] for attr in user["Attributes"] if attr["Name"] == "preferred_username"),None
    dict_users[handle[0]] = sub[0]
    print(dict_users)


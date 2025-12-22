#!/usr/bin/env python3
import psycopg
import os
import sys

connection_url = "postgresql://thinkspace.c32ye0guaums.eu-west-2.rds.amazonaws.com/thinkspace"
conn = None
try:
    print('attempting connection' )
    conn = psycopg.connect(connection_url)
    print("Connection successful!")
except psycopg.Error as e:
    print ("Unable to connect to the database:", e)
finally:
    conn.close()
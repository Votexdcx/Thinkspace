from psycopg_pool import ConnectionPool
import os

#connection_url = os.getenv("CONNECTION_URL")
connection_url = "postgresql://Thinkspacedb:quwrem-firjyz-vipmA7@thinkspace.c32ye0guaums.eu-west-2.rds.amazonaws.com:5432/thinkspace"
pool = ConnectionPool(conninfo=connection_url)

def query_wrap_object(template):
    sql = f"""
    SELECT COALESCE(row_to_json(object_row), '{{}}'::json)
    FROM (
      {template}
    ) object_row;
    """
    return sql

def query_wrap_array(template):
    sql = f"""
    SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))), '{{}}'::json)
    FROM (
      {template}
    ) array_row;
    """
    return sql
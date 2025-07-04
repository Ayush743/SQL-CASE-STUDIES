import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="prime"
)
cursor=connection.cursor()
def display_query(q):
    return pd.read_sql(q,connection)

import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="live_class"
)
cursor=connection.cursor()
def display_record(q):
    print( pd.read_sql(q,connection))

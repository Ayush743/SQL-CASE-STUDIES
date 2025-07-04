import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="amazon_ecommerce"
)
cursor=connection.cursor()
#<<<<<<<<<<<<<<<<<------------creating table----------------------->>>>>>>>>>>>>>>
query1='create table customer(c_id int primary key auto_increment,first_name varchar(255) not null, last_name varchar(255), email varchar(255) not null,gender varchar(20) ,country varchar(255) not null)'
query2='create table orders(o_id integer primary key auto_increment,o_name varchar(255) not null,order_date datetime not null,shipping_date datetime not null,delivery_date datetime not null,total_amount decimal)'

#<<<<<<<<<<-------------------Executing the queries---------------------->>>>>>>>>.
# cursor.execute(query1)
# cursor.execute(query2)
"""<<<<<<<<--------------Joins---------------->>>>>>>>>>>>>>"""
# Joins in mysql are used to combine two or more tables based on common or related column between them

"""Benfits of using distributed table instead of combining all the records and fields in single table"""
# it lead to data redudancy annd repeatition
# data is not organize properly and lead to update anamoly

"""Types of joins"""
# There are 6 types of join in mysql
# 1)inner join
# 2)full outer join
# 3)left join
# 4)right join
# 5)self join
# 6)cross join



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

#-----displaying the tables------>>>>>
q1='show tables;'
# display_record(q1)

"""<<<<<<<---------cross join ----------->>>>>>>>>>>>>>"""
q2='select * from live_class.users1 u cross join live_class.groups g '
# display_record(q2)

"""<<<<<<------------inner join----------------->>>>>>>>"""
q3='select * from users1 t1 inner join membership t2 on t1.user_id=t2.user_id '
display_record(q3)

"""<<<<<<<--------------left join ---------------->>>>>>>>>>>>"""
q4='select * from membership t1 left join users1 t2 on t1.user_id=t2.user_id;'
# display_record(q4)

"""<<<<<<<<<,------------right join----------->>>>>>>>>>>>>>>"""
q5='select * from membership t1 right join users1 t2 on t1.user_id=t2.user_id ;'
display_record(q5)

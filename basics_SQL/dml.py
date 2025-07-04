
import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="amazon_ecommerce"
)
cursor=connection.cursor()




#<<<<<<<<<<<<<<----------DML(Data Manipulation Command)----------------------->>>>>>>>>>>>>>>>>>>>>>>>>>
"""<<<<<<<<<<<<---------------------Insert query-------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>."""
#<<<<<<<<<<<<<--------------inserting data----------------------->>>>>>>>>>>>
query='insert into customer values(10001,"Hinata","Hyuga","hinata113@gmail.com","f","india")'
query2='''insert into customer(first_name,last_name,email,gender,country) values("Naruto","Uzumaki","naruto007@gmail.com","m","Japan"),
("Sakura","Haruno","sakura.pink@gmail.com","f","Japan"),
("Sasuke","Uchiha","uchiha.shadow@gmail.com","m","South Korea"),
("Itachi","Uchiha","itachi.crow@gmail.com","m","Germany"),
("Shikamaru","Nara","shika.lazy@gmail.com","m","India")
'''


#--------------------query execution---------------------->


# cursor.execute(query)
# cursor.execute(query2)
# connection.commit()




"""<<<<<<<<<<<<<---------------------2) Retrieve Query------------------------>>>>>>>>>>>>>>>"""
#<<<<<<<<<<<<<<<<--------------------Displaying the records by querying using pandas---------------->>>>>>>>>>
q1='select * from customer'
df = pd.read_sql(q1, connection)
# print(df)


#---lets create a function to display record instead of wrting again and again-------->

def display_record(q):
    return pd.read_sql(q,connection)




#<<<<<<<<<,-----for displaying limited number of records use keyword 'limit'------------------>>>>>>>
q='select * from customer limit 5' # display only 5 records from top
print(display_record(q))





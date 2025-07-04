import mysql.connector
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="flipkart"
)
cursor=connection.cursor()
def display_record(q):
     print(pd.read_sql(q,connection))

"""<<<<<<<--------Displaying tables------->>>>>>>>>>"""
q1='show tables;'
# display_record(q1)
"""output"""
# 0           category
# 1      order_details
# 2             orders
# 3              users



"""<<<<<<-----------find all profitable orders--------->>>>>>>>"""
q1='select t1.order_id,sum(profit) as total_profit from orders t1 join order_details t2 on t1.order_id=t2.order_id group by t1.order_id having total_profit>0 order by total_profit desc;'
# display_record(q1)



"""<<<<<------find the customer who has placed maximum no of orders------------>>>>>>>"""
q2='select name,count(*)as num_of_orders from users t1 join orders t2 on t1.user_id=t2.user_id group by name order by num_of_orders desc limit 1 ;'
# display_record(q2)


"""<<<<---------------Which is the most profitable category------------>>>>>>>>>>>>>>>>>>"""
q3='select sum(profit) as total_profit,vertical as category from order_details t1 join category t2 on t1.category_id=t2.category_id group by vertical order by total_profit desc limit 1 '
# display_record(q3)

"""<<<<<<<----------which is the most profitable state-------->>>>>>>>."""
q4='select state,sum(profit) as total_profit from users t1 join orders t2 on t1.user_id=t2.user_id join order_details t3 on t2.order_id=t3.order_id group by state order by total_profit desc '
# display_record(q4)

"""<<<<<<<<<----------------find all the categories with profit here than 3000"""
q5='select sum(profit) as total_profit,vertical as category from order_details t1 join category t2 on t1.category_id=t2.category_id group by vertical having total_profit>3000 order by total_profit desc'
# display_record(q5)
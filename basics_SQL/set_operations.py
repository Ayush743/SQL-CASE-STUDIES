

"""<<<<<-------------See the tables in the dataset folder------------------>>>>>>."""



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

"""<<<<<<<<<<<<----------Union-------------->>>>>>>>>>>>>>."""
# used to combine the result of two or more select statements into a single set result and remove the duplicate rows or records

q1='select * from person1 union select * from person2'
# display_record(q1)
"""
output :-  
"""
#    id     name
# 0   1    Alice
# 1   2      Bob
# 2   3  Charlie
# 3   4    David
# 4   5    Emily
# """

"""<<<<<<<<<<<<----------Union All-------------->>>>>>>>>>>>>>."""

# used to combine the result of two or more select statements into a single set result and  do not rempve remove the duplicate rows or records
q2='select * from person1 union all select * from person2'
display_record(q2)

""" output:-"""
#   id     name
# 0   1    Alice
# 1   2      Bob
# 2   3  Charlie
# 3   3  Charlie
# 4   4    David
# 5   5    Emily

"""<<<<<<<<<<<<----------Intersect-------------->>>>>>>>>>>>>>."""
q3='select * from person1 intersect select * from person2'
# display_record(q3)
""" output:-"""
#    id     name
# 0   3  Charlie


"""<<<<<<<<<<<<----------Except-------------->>>>>>>>>>>>>>."""
q4='select * from person1 except select * from person2'
display_record(q4)
""" output:-"""
#     id   name
# 0   1  Alice
# 1   2    Bob
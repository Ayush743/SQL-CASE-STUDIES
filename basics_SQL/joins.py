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

"""<<<<<<--------output----->>>>>>>"""
# 0                class
# 1               groups
# 2           membership
# 3              person1
# 4              person2
# 5               users1



"""<<<<<<<---------cross join ----------->>>>>>>>>>>>>>"""

q2='select * from live_class.users1 u cross join live_class.groups g '

# display_record(q2)

"""<<<<<<--------output----->>>>>>>"""

#     user_id     name  age  emergency_contact  group_id group_name
# 0         1   Nitish   34                 11         7    Group 7
# 1         1   Nitish   34                 11         3    Group 3
# 2         1   Nitish   34                 11         2    Group 2
# 3         1   Nitish   34                 11         1    Group 1
# 4         2    Ankit   32                  1         7    Group 7
# 5         2    Ankit   32                  1         3    Group 3
# 6         2    Ankit   32                  1         2    Group 2
# 7         2    Ankit   32                  1         1    Group 1
# 8         3     Neha   23                  1         7    Group 7
# 9         3     Neha   23                  1         3    Group 3
# 10        3     Neha   23                  1         2    Group 2
# 11        3     Neha   23                  1         1    Group 1
# 12        4  Radhika   34                  3         7    Group 7
# 13        4  Radhika   34                  3         3    Group 3
# 14        4  Radhika   34                  3         2    Group 2
# 15        4  Radhika   34                  3         1    Group 1
# 16        8  Abhinav   31                 11         7    Group 7
# 17        8  Abhinav   31                 11         3    Group 3
# 18        8  Abhinav   31                 11         2    Group 2
# 19        8  Abhinav   31                 11         1    Group 1
# 20       11    Rahul   29                  8         7    Group 7
# 21       11    Rahul   29                  8         3    Group 3
# 22       11    Rahul   29                  8         2    Group 2
# 23       11    Rahul   29                  8         1    Group 1





"""<<<<<<------------inner join----------------->>>>>>>>"""

q3='select * from users1 t1 inner join membership t2 on t1.user_id=t2.user_id '

# display_record(q3)

"""<<<<<<--------output----->>>>>>>"""


#    user_id     name  age  emergency_contact  membership_id  group_id  user_id
# 0        1   Nitish   34                 11              1         1        1
# 1        2    Ankit   32                  1              2         1        2
# 2        3     Neha   23                  1              3         1        3
# 3        4  Radhika   34                  3              4         1        4
# 4        1   Nitish   34                 11              5         2        1
# 5        4  Radhika   34                  3              6         2        4
# 6        1   Nitish   34                 11              7         3        1
# 7        3     Neha   23                  1              8         3        3
# 8        1   Nitish   34                 11              9         4        1



"""<<<<<<<--------------left join ---------------->>>>>>>>>>>>"""

q4='select * from membership t1 left join users1 t2 on t1.user_id=t2.user_id;'

# display_record(q4)

"""<<<<<<--------output----->>>>>>>"""

#     membership_id  group_id  user_id  user_id     name   age  emergency_contact
# 0               1         1        1      1.0   Nitish  34.0               11.0
# 1               2         1        2      2.0    Ankit  32.0                1.0
# 2               3         1        3      3.0     Neha  23.0                1.0
# 3               4         1        4      4.0  Radhika  34.0                3.0
# 4               5         2        1      1.0   Nitish  34.0               11.0
# 5               6         2        4      4.0  Radhika  34.0                3.0
# 6               7         3        1      1.0   Nitish  34.0               11.0
# 7               8         3        3      3.0     Neha  23.0                1.0
# 8               9         4        1      1.0   Nitish  34.0               11.0
# 9              10         1        5      NaN     None   NaN                NaN
# 10             11         1        6      NaN     None   NaN                NaN



"""<<<<<<<<<,------------right join----------->>>>>>>>>>>>>>>"""

q5='select * from membership t1 right join users1 t2 on t1.user_id=t2.user_id ;'

display_record(q5)

"""<<<<<<--------output----->>>>>>>"""


#     membership_id  group_id  user_id  user_id     name  age  emergency_contact
# 0             9.0       4.0      1.0        1   Nitish   34                 11
# 1             7.0       3.0      1.0        1   Nitish   34                 11
# 2             5.0       2.0      1.0        1   Nitish   34                 11
# 3             1.0       1.0      1.0        1   Nitish   34                 11
# 4             2.0       1.0      2.0        2    Ankit   32                  1
# 5             8.0       3.0      3.0        3     Neha   23                  1
# 6             3.0       1.0      3.0        3     Neha   23                  1
# 7             6.0       2.0      4.0        4  Radhika   34                  3
# 8             4.0       1.0      4.0        4  Radhika   34                  3
# 9             NaN       NaN      NaN        8  Abhinav   31                 11
# 10            NaN       NaN      NaN       11    Rahul   29                  8



"""<<<<<<<<<,------------full outer join----------->>>>>>>>>>>>>>>"""

q6='select * from membership t1 left join users1 t2 on t1.user_id=t2.user_id union select * from membership t1 right join users1 t2 on t1.user_id=t2.user_id '

display_record(q6)

"""<<<<<<--------output----->>>>>>>"""

#     membership_id  group_id  user_id  user_id     name   age  emergency_contact
# 0             1.0       1.0      1.0      1.0   Nitish  34.0               11.0
# 1             2.0       1.0      2.0      2.0    Ankit  32.0                1.0
# 2             3.0       1.0      3.0      3.0     Neha  23.0                1.0
# 3             4.0       1.0      4.0      4.0  Radhika  34.0                3.0
# 4             5.0       2.0      1.0      1.0   Nitish  34.0               11.0
# 5             6.0       2.0      4.0      4.0  Radhika  34.0                3.0
# 6             7.0       3.0      1.0      1.0   Nitish  34.0               11.0
# 7             8.0       3.0      3.0      3.0     Neha  23.0                1.0
# 8             9.0       4.0      1.0      1.0   Nitish  34.0               11.0
# 9            10.0       1.0      5.0      NaN     None   NaN                NaN
# 10           11.0       1.0      6.0      NaN     None   NaN                NaN
# 11            NaN       NaN      NaN      8.0  Abhinav  31.0               11.0
# 12            NaN       NaN      NaN     11.0    Rahul  29.0                8.0


"""<<<<<<<<<,------------self join----------->>>>>>>>>>>>>>>"""
q7='select t2.name,t1.name as emergency_contact from users1 t1  join users1 t2 on t1.user_id=t2.emergency_contact; '
display_record(q7)
"""<<<<<<<<<<------output---------------->>>>>>>>>>"""
#       name emergency_contact
# 0   Nitish             Rahul
# 1    Ankit            Nitish
# 2     Neha            Nitish
# 3  Radhika              Neha
# 4  Abhinav             Rahul
# 5    Rahul           Abhinav
 
 #<------------another example ( joining more than two columns)---------->>>>>>>>>>>>>>>>
q8='select first_name,last_name,class_name,teacher from students s  join class c on s.class_id=c.class_id and s.enrollment_year=c.class_year;'

display_record(q8)

"""<<<<<<-----output--------->>>>>>>>>"""
#   first_name last_name class_name    teacher
# 0       John     Smith   Math 101  Mr. Smith
# 1        Bob   Johnson   Math 101  Mr. Smith
# 2      Sally     Brown  Science 1    Dr. Lee

import mysql.connector

#In the below code one can observe there is a extra argument which is database as the name suggest
#it is used to select the database on which on wants to execute a query
mydatabase = mysql.connector.connect(host='localhost',user='root',password='Hello World!',database='adarshdb')

mycursor = mydatabase.cursor()

# Below is the code to create table in the above mention database
mycursor.execute("create table employee(name varchar(200),salary int(20))")

# #Below code is to see the available tables in the database
# mycursor.execute("show tables")
#
# for tables in mycursor:
#     print(tables)
import mysql.connector

mydatabase = mysql.connector.connect(host="localhost",user="root",password="Hello World!")

#after establishing the connection one must create a cursor object so that he/she can exectute the mysql
#queries with it
mycursor =  mydatabase.cursor()

#code to create database in mysql or mysql workbench in
#mycursor.execute("create database adarshdb")

#as the code suggest it is execute show databases query
mycursor.execute("show databases")

#this for loop is to print all the databases that are available in the system mysql
for db in mycursor:
    print(db)


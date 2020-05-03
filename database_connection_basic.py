
#Inorder to establish the connection one must import this package
import mysql.connector

#After that in one variable one must keep the connection link which include host which is local host
# user name which is refered by user (in  my case it is root which is default to the mysql)
#password which can be refered either by passwd or password
mydatabase = mysql.connector.connect(host="localhost",user="root",password="Hello World!")

print(mydatabase)


#This condition statement is to check whether the connection has established or not between mysql and out python file
if(mydatabase):
    print("connection established")

else:
    print("connection doesn't established")
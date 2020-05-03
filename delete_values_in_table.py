import mysql.connector

mydatabase = mysql.connector.connect(host='localhost',user='root',password='Hello World!',database='adarshdb')

mycursor = mydatabase.cursor()

#Here I have observed one thing that in table
# the name was Bhargavi but I have given bhargavi but the value got deleted
#and one more thing to notice is one must commit the changes inorder to make them apply

query='delete from employee where name="adarsh"'

mycursor.execute(query)

#mydatabase.commit()
#Here if we don't commit even though here it may show as the value got deleted
#but in actual table or in other program value still exists in the table and the database

mycursor.execute('select * from employee')

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
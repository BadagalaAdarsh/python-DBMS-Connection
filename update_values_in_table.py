import mysql.connector

mydatabase = mysql.connector.connect(host='localhost',user='root',password='Hello World!',database='adarshdb')

mycursor = mydatabase.cursor()

query = "update employee set salary=100000 where name = 'Jyothsna'"

mycursor.execute(query)

mydatabase.commit()
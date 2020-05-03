import mysql.connector

mydatabase = mysql.connector.connect(host='localhost',user='root',passwd='Hello World!',database='adarshdb')

mycursor = mydatabase.cursor()

# mycursor.execute('select name from employee')
#
# #fetchone is the first function of the read operation
# #what it is going to do is,  it is going to fetch one value from the column "name" under the employee table
# myresult = mycursor.fetchone()
#
# #when below loop is runned it is going to print only adarsh as it was the first value that was inserted into the table
# for row in myresult:
#     print(row)


# A thing to observe here is that when both above commented code and below code is runned it gives so many errors
# I need to find it out why


#Instead of execute one cannot replace with execute many
mycursor.execute('select * from employee')

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

#Above for loop prints the following as the result
#('adarsh',50000)
#('dhamaresh',60000)
#('Jyothsna',90000)
#('Bhargavi',75000)
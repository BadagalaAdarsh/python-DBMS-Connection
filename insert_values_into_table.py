import mysql.connector

mydatabase = mysql.connector.connect(host='localhost',user='root',passwd='Hello World!',database='adarshdb')

mycursor = mydatabase.cursor()

#Here I have created a variable sqlform to hold the sql query in it which is supposed to insert values into the table create before
#Here %s are nothing but placeholders   One can replace them anytime with anyother value
sqlform = 'insert into employee (name,salary) values (%s,%s)'

#here a tuple is created because after wards when we are doing the read operation we are going to make use of two fetch functions
# there is a one fetch function called fetch all
#Making use of fetch all we need not populate table with the single value because that'll not be good

#Here employees hold values of four employees with their names and salaries
employees = [("adarsh",50000),("dhamaresh",60000),("Jyothsna",90000),("Bhargavi",75000)]

#Here execute many is used because we are not going to insert a single value
#here we are making use of tuples which holds mulitple values so it is better to use executemany
mycursor.executemany(sqlform,employees)

#This is to save the changes from the last executed statement
mydatabase.commit()

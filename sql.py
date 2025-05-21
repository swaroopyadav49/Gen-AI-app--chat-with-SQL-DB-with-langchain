# This file is responsible for creating the Database, creating the Table, Inserting all specific records.  

import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve 
cursor=connection.cursor()

## create the table
table_info="""
Create table if not exists STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

# For Creating the Table we have a command like 

cursor.execute(table_info) 

## Insert some more records

               
cursor.execute('''Insert Into STUDENT values('Swaroop','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Joshua','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Minni','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vasudeva','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Kumar','DEVOPS','A',35)''')

## Dispaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
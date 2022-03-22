import sqlite3
from tabulate import tabulate

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
 sql_command = """CREATE TABLE table2 (
 a VARCHAR(20),
 b INTEGER PRIMARY KEY,
 c VARCHAR(30)
);"""

# execute the statement
crsr.execute(sql_command)
# SQL command to insert the data in the table
sql_command = """INSERT INTO table2 VALUES (1,2,3);"""
crsr.execute(sql_command)
  
# # another SQL command to insert the data in the table
# sql_command = """INSERT INTO table2 VALUES (4,5,6);"""
# crsr.execute(sql_command)
  
# # To save the changes in the files. Never skip this.
# # If we skip this, nothing will be saved in the database.
# connection.commit()

# close the connection
crsr = connection.cursor()
  
# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM table2")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  
# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
for i in ans:
    print(i)

import csv
import os



class Project:
    def __init__(self,name):
        self.name=name
    dic={}
    def raw1(self):
    #opening a file
        f=open(self.name,"r")
            #reading lines in csv file
        lines=f.readlines()
#creating a empty dictionary
    def raw1(self):
        header1=self.lines[:1]
        head=header1[0].strip()
        head=head.split(",")
        return head


    def raw2(self):
        dic={}
        rows=self.lines[1:]

        # reading each line in rows
        for row in rows:
            row=row.strip()
            values=row.split(" ")
            values=values[0].split(",")
            i=0
            # appending values to respective key in dictionary
            for val in values:
                dic.setdefault(self.head[i],[])
                dic[self.head[i]].append(val)
                i+=1
        return dic

obj=Project("a2.csv")
print(obj.func())
print(tabulate(ans, headers=obj.func(), tablefmt='psql'))

connection.close()

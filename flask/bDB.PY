import sqlite3
con=sqlite3.connect('database3.db')
print('opened database succesfull')
con.execute('CREATE TABLE book(name char(20),author char(20),pdf char(20));')
print('Table created succesfully')
con.close()
#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
Module that lists all states from the database using MySQL
"""

db = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    password=argv[2],
    port=3306,
    db=argv[3]
    )

cursor = db.cursor()  # cursor object is used 4 execution of sql queries
cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
mydata = cursor.fetchall()

for row in mydata:
    print(row)

cursor.close()
db.close()

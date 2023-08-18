#!/usr/bin/python3
"""
modules that lists all states with a name starting with N
from the database, connect with MySQLdb
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
              LIKE BINARY 'N%'ORDER BY states.id ASC""")
    mydata = c.fetchall()

    for row in mydata:
        print(row)

    c.close()
    db.close()

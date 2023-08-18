#!/usr/bin/python3
"""
A script that takes in an argument and displays all modules in the
state table where name matches the argument
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
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
              ORDER BY states.id ASC".format(sys.argv[4]))

    mydata = c.fetchall()

    for row in mydata:
        print(row)

    c.close()
    db.close()

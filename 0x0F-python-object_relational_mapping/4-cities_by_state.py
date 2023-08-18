#!/usr/bin/python3
"""
script that lists all cities, module used MySQLdb
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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
              INNER JOIN states ON state_id = states.id")
    mydata = c.fetchall()
    for row in mydata:
        print(row)

    c.close()
    db.close()

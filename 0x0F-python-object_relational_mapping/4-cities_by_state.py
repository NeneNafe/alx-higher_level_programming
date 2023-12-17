#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa
"""


def lists_cities():
    """Gives access to the db and get the cities from the db"""
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cmdquery = 'SELECT cities.id, cities.name, states.name \
        FROM cities INNER JOIN states ON states.id=cities.state_id'
    cursor = db.cursor()
    cursor.execute(cmdquery)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    lists_cities()

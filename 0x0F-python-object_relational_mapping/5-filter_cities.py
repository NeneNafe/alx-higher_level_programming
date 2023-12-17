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
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cmdquery = 'SELECT cities.name FROM \
        cities INNER JOIN states ON states.id=cities.state_id \
        WHERE states.name=%s'
    cursor = db.cursor()
    cursor.execute(cmdquery, (state_name,))
    rows = cursor.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    cursor.close()
    db.close()


if __name__ == "__main__":
    lists_cities()

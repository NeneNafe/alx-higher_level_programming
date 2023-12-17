#!/usr/bin/python3
"""a script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa
"""


def stateswithN():
    """Gives access to the db and get the states from the db
    that satre with the letter N"""
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
    cmdquery = f'SELECT * FROM states WHERE name LIKE BINARY "N%" \
        ORDER BY states.id ASC'
    cursor = db.cursor()
    cursor.execute(cmdquery)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    stateswithN()

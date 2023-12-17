#!/usr/bin/python3
"""a script that lists all states from thedatabase hbtn_0e_0_usa
"""


def mylinkedstates():
    """Gives access to the db and get the states frome the db"""
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
    cmdquery = f'SELECT DISTINCT * FROM states ORDER BY id ASC'
    cursor = db.cursor()
    cursor.execute(cmdquery)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    mylinkedstates()

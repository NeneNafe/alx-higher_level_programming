#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""


def searchedstate():
    """Gives access to the db and get the states from the db
    that are searched"""
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    srchd_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cmdquery = ('SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY \
        states.id ASC'.format(srchd_name))
    cursor = db.cursor()
    cursor.execute(cmdquery)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    searchedstate()

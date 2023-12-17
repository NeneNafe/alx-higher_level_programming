#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument by invoking injection
"""


def free_injection():
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
    cmdquery = f'SELECT * FROM states WHERE name LIKE %s'
    cursor = db.cursor()
    cursor.execute(cmdquery, (srchd_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    free_injection()

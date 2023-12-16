#!/usr/bin/python3
"""a script that lists all states from thedatabase hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Gives access to the db and get the states frome the db"""
    connect_db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = connect_db.cursor()

    db_cursor.execute("SELECT * FROM sates")

    rows_selected = db_cursor.fetchall()

    for row in row_selected:
        print(row)

#!/usr/bin/python3

"""
List all data(states) from state Table order
by the id.
(args) a gotten from sys.argv without check
"""


import sys
import MySQLdb


if __name__ == "__main__":

    db_conn = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              host='localhost',
                              port=3306)

    cursr = db_conn.cursor()

    cursr.execute("SELECT * FROM states ORDER BY states.id ASC")

    results = cursr.fetchall()

    for row in results:
        print(row)

    cursr.close()
    db_conn.close()

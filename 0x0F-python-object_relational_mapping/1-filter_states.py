#!/usr/bin/python3

"""
Lst all data(stats) frm stat Tbl that start
with 'N' ordr by the id.
(args) a gotten from sys.argv without chck
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

    query = """SELECT * FROM states WHERE
            name LIKE BINARY 'N%' ORDER BY id ASC"""
    cursr.execute(query)

    results = cursr.fetchall()

    for row in results:
        print(row)

    cursr.close()
    db_conn.close()

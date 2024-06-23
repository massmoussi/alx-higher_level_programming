#!/usr/bin/python3

"""
    Script Extract All rw of data(data)
    frm state Tbl If Exist
    parameterized queries to prevent SQLi
    (args) are received frm sys.argv
"""


import sys
import MySQLdb


if __name__ == "__main__":

    db_conn = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              host='localhost',
                              port=3306)

    state = sys.argv[4]
    cursr = db_conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursr.execute(query, (state,))

    results = cursr.fetchall()

    for row in results:
        print(row)

    cursr.close()
    db_conn.close()

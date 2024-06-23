#!/usr/bin/python3

"""
    Script Extract All row of data(data)
    frm stat Tble If Exst
    (args) are received frm sys.argv witht Chck
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

    cursr.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{}' "
                "ORDER BY id ASC".format(state))

    results = cursr.fetchall()

    for row in results:
        print(row)

    cursr.close()
    db_conn.close()

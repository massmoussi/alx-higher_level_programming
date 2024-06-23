#!/usr/bin/python3

"""
    Script Extract All cities
    within in certain stat
    the Script is Using aliasing
    (args) received frm sys.argv
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
    query = """SELECT c.id, c.name, s.name
               FROM states AS s, cities AS c
               WHERE c.state_id = s.id
               ORDER BY c.id ASC"""
    cur.execute(query)

    results = cursr.fetchall()

    for row in results:
        print(row)

    cursr.close()
    db_conn.close()

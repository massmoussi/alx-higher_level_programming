#!/usr/bin/python3

"""
    Script Extract All cities
    within in certain state
    the Script is Using JOIN
    (args) received from sys.argv
"""


import sys
import MySQLdb


if __name__ == "__main__":

    db_conn = MySQLdb.connect(user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              host='localhost',
                              port=3306)

    cur = db_conn.cursor()
    state = sys.argv[4]
    query = """SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s ORDER BY cities.id ASC"""
    cur.execute(query, (state,))

    results = cur.fetchall()

    print(", ".join([row[0] for row in results]))

    cur.close()
    db_conn.close()

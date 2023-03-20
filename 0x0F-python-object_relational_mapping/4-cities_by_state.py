#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
'''
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT a.id, a.name, b.name
                FROM cities AS a
                INNER JOIN states AS b
                ON a.state_id = b.id")
    state = cur.fetchall()

    for s in state:
        print(s)

    cur.close()
    conn.close()

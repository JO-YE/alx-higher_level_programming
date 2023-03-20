#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument
and lists all cities of that state
'''
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT a.id, a.name, b.name\
                FROM cities AS a\
                INNER JOIN states AS b\
                ON a.state_id = b.id\
                WHERE b.name = %s", (sys.argv[4],))
    state = cur.fetchall()

    for s in state:
        print(", ".join([city[1] for city in cities]))

    cur.close()
    conn.close()

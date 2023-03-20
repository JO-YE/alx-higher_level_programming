#!/usr/bin/python3
'''
a script that list all states from the databases hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states')
    state = cur.fetchall()

    for s in state:
        print(s)

    cur.close()
    conn.close()

#!/usr/bin/python3
'''
a script that list all states with name starting with N
'''
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE BINARY name LIKE 'N%'')
    state = cur.fetchall()

    for s in state:
        print(s)

    cur.close()
    conn.close()

#!/usr/bin/python3
'''A script that list all cities from the database hbtn_0e_4_usa.'''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM cities')
    lists = cur.fetchall()

    for l in lists:
        print(l)

    cur.close()
    db.close()

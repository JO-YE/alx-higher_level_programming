#!/usr/bin/python3
'''a python scipt that takes in a url and display value of a specified
   header parameter
'''
import urllib.parse
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get("X-Request-Id"))

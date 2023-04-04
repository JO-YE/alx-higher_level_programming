#!/usr/bin/python3
'''a script that display the value of a variable in the response header
'''
import requests
import sys


if __name__ == "__main__":
    reqs = requests.get(sys.argv[1]).headers
    print(reqs.get("X-Request-Id"))

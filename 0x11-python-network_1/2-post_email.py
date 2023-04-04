#!/usr/bin/python3
'''script that takes in a URL and an email
   sends a POST request to the passed URL with the email as a parameter
'''
import urllib.parse
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))

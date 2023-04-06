#!/usr/bin/python3
'''script that takes in a URL and an email
   sends a POST request to the passed URL with the email as a parameter
'''
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    datas = {'email': sys.argv[2]}

    req = requests.post(url, data=datas)
    print(req.text)

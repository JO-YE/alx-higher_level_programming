#!/usr/bin/pyhton3
'''a script that send a request to a URL, display the response
   as well as a compition for Http status code.
'''
import requests
import sys


if __name__ == '__main__':
    respon = requests.get(sys.argv[1])
    code = repon.status_code

    if respon.status_code >= 400:
        print('Error code: {}'.format(code))

#!/usr/bin/python3
''' script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        datas = {'q': ''}
    else:
        datas = {'q': sys.argv[1]}

    res = requests.post('http://0.0.0.0:5000/search_user', data=datas)

    try:
        if res.json() == {}:
            print('No result')
        else:
            res_id = res.get('id')
            res_id = res.get('name')
            print(f'[{res_id}] {res_id}')
    except ValueError:
        print('Not a valid JSON')

#!/usr/bin/python3
'''a python script that fetches a url using requests package'''
import requests


if __name__ == '__main__':
    content = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(content.text)))
    print(f'\t- content: {content.text}')

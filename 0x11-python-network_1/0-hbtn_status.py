#!/usr/bin/python3
# a python script that fetches a url using urllib
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content.decode("utf-8")}')

#!/usr/bin/python3

'''Module contain fxn that convert python to JSON.'''

import json

def to_json_string(my_obj):
    '''A function that returns the JSON representation of an object.'''
    y = json.dumps(my_obj)
    print(y, end='')

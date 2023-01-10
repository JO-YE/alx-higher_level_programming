#!/usr/bin/python3

'''Module contain fxn that convert JSON to python.'''
import json


def from_json_string(my_str):
    '''A function that returns an object (Python) rep by json string.'''
    y = json.loads(my_str)
    return y

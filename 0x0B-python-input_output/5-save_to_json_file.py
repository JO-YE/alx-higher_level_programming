#!/usr/bin/python3

'''Module contain fxn that write and obj to a file.'''
import json


def save_to_json_file(my_obj, filename):
    y = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(y)

#!/usr/bin/python3

'''Module contain fxn that write and obj to a file.'''
import json


def save_to_json_file(my_obj, filename):
    '''A function that writes an Object to a text file, usinf json as rep.'''
    with open(filename, 'w', encoding='utf-8') as f:
        y = json.dumps(my_obj)
        return f.write(y)

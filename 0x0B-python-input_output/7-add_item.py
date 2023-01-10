#!/usr/bin/python3

'''Module contain fxn that add arg. to a python list.'''
from sys import argv


write_into_file = __import__('5-save_to_json_file').save_to_json_file
create_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        lst = create_file(add_item.json)
    except:
        pass
        lst = []
    for arg in argv[1:]:
        lst.append(arg)
    write_into_file(lst, 'add_item.json')

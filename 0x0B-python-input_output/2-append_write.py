#!/usr/bin/python3

'''Module that contain fxn that append a string at the end of a file.'''


def append_write(filename="", text=""):
    '''A function that appends a string at the end of a text file
    and returns the number of characters added.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

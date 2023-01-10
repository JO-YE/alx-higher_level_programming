#!/usr/bin/python3

'''Input/Output functions.'''


def write_file(filename="", text=""):
    '''Function that writes a string to a text file
    and returns the number of chaaracters written.
    '''
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)

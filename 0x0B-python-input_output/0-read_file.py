#!/usr/bin/python3

'''Tasks on input/output functions.'''


def read_file(filename=""):
    '''A function that reads a text file and prints it to stdout.'''
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')

#!/usr/bin/python3

'''This module consist of a fxn that print lines.'''


def text_indentation(text):
    '''Function that prints a text with 2 lines after , ? and :.'''
    if type(text) != str:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print()
            print()
            i += 1
            if text[i] != ' ':
                i -= 1
        i += 1

#!/usr/bin/python3

'''Module contain fxn that returns the list of attri and method.'''


def lookup(obj):
    '''A function that returns the list of available attributes
    and methods of an object.
    '''
    return dir(obj)

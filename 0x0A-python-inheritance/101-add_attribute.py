#!/usr/bin/python3

'''Module contain fxn that add attri to object.'''


def add_attribute(obj, name, value):
    '''A function that adds a new attribute to an object.'''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

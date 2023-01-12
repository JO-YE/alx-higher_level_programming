#!/usr/bin/python3

'''Module contain fxn that check for class subclass.'''


def inherits_from(obj, a_class):
    '''A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.
    '''
    if type(obj) == a_class:
        return False
    else:
        return True

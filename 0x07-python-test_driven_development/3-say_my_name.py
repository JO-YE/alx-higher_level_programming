#!/usr/bin/python3

'''This module consist of fxn that print names.'''


def say_my_name(first_name, last_name=""):
    '''Function that prints
    My name is <first name> <last name>

    Args:
        first_name: first name of user
        last_name: last name of user

   Returns:
        No return

    Raises:
        TypeError: if name is not string.

    '''
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))

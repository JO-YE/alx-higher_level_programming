#!/usr/bin/python3

"""Class LockedClass that avoids dynmaically created attributes."""


class LockedClass:
    '''
    Prevent users from creating any other obj attribute except
    except if the new instance attribute is called first_name.
    '''
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass

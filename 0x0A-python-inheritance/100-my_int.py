#!/usr/bin/python3

'''Module contain class that inherit from int.'''


class MyInt(int):
    '''A class MyInt that inherits from int.'''
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)

#!/usr/bin/python3

'''Module that define a class.'''


class BaseGeometry:
    '''A class BaseGeometry.'''
    def area(self):
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

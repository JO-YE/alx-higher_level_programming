#!/usr/bin/python3

'''Module that define subclass base on the parent class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A class Rectangle that inherits from BaseGeometry.'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', height)
        self.integer_validator('height', width)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))

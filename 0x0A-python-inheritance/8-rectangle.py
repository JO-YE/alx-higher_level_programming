#!/usr/bin/python3

'''Module that define a class that inherit from anothor class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A class Rectangle that inherits from BaseGeometry.'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

#!/usr/bin/python3

'''Defining a class Rectangle.'''
from models.base import 


class Rectangle(Base):
    '''Class Rectangle that inherits from Base.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

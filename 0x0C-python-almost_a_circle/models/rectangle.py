#!/usr/bin/python3

'''Defining a class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle that inherits from Base.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializing.'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Width getter.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter.'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Height getter.'''
        return self.__height

    @height.setter
    def height(self,value):
        '''Height setter.'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''X getter.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''X setter.'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Y getter.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Y setter.'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Return the area of a Rectangle."""
        return (self.height * self.width)

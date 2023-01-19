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
    def get_width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def set_width(self):
        ''' width setter '''
        self.__width = width

    @property
    def get_height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def set_height(self):
        ''' height setter '''
        self.__height = height

    @property
    def get_x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def set_x(self):
        ''' x setter '''
        self.__x = x

    @property
    def get_y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def set_y(self):
        ''' y setter '''
        self.__y = y

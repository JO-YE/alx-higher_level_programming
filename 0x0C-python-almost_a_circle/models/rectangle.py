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

    def get_width(self):
        ''' width getter '''
        return self.__width

    def set_width(self):
        ''' width setter '''
        self.__width = width

    def get_height(self):
        ''' height getter '''
        return self.__height

    def set_height(self):
        ''' height setter '''
        self.__height = height

    def get_x(self):
        ''' x getter '''
        return self.__x

    def set_x(self):
        ''' x setter '''
        self.__x = x

    def get_y(self):
        ''' y getter '''
        return self.__y

    def set_y(self):
        ''' y setter '''
        self.__y = y

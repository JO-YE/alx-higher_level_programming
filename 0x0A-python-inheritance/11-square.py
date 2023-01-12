#!/usr/bin/python3

'''Module that define subclass base on the parent class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A class Square that inherits from subclass Rectangle.'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__size, self.__size))

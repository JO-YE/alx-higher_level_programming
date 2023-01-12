#!/usr/bin/python3

'''Module define a class square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A class Square that inherits from Rectangle.'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size

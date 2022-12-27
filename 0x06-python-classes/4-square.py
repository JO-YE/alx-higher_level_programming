#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Define a square using setter and getter."""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integar")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integar")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This method returns the square area of the object."""
        return (self.__size ** 2)

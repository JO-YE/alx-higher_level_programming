#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Public instance method."""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integar")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method returns the square area of the object."""
        return (self.__size ** 2)

#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Define a square using setter and getter."""
    def __init__(self, size=0):
        if (type(size) != int) and (type(size) != float):
            raise TypeError("size must be an integer")
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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.__size != other.__size

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.__size < other.__size

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.__size <= other.__size

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.__size > other.__size

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.__size >= other.__size

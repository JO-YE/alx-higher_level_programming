#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Public instance method."""
    def __init__(self, size):
        self.__size = size
    def area(self):
        return self.__size ** 2)

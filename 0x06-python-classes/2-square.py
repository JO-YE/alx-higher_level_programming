#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Private attribute 'size' must be an integer.
    Otherwise raise a TypeError.
    If size is less than 0, raise a ValueError.
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Private attribute 'size' must be an integar.
    Otherwise raise a TypeError.
    If size is less than 0, raise a ValueError.
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integar")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

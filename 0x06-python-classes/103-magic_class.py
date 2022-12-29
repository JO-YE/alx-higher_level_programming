#!/usr/bin/python3

"""Class MagicClass for python Bytecode."""

import math


class MagicClass:
    """Class that stores properties of a circumference."""
    def __init__(self, radius=0):
        if (type(radius) != int) and (type(radius) != float):
            raise TypeError('radius must be a number')
    self.__radius = radius

    def area(self):
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)

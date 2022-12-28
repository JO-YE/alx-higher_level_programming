#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Continuation from 4-...py in addition with a pub.obj method."""
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        """Property to retrive it."""
        return self.__size
    @size.setter
    def size(self, value):
        """Property setter to set it."""
        if not type(value) is int:
            raise TypeError("size must be an integar")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return (self.size ** 2)

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("#", end='')
                print()

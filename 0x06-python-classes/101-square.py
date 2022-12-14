#!/usr/bin/python3

"""Representing class Square."""


class Square:
    """Continuation from 6-..py."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError('size must be integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property to retrive it."""
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[0]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[1]) is int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return (self.size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")

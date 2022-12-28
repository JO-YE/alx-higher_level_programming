#!/usr/bin/python3

"""Representing a class Square."""


class Square:
    """Continuation from 4-...py in addition with a pub.obj method."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive intege
rs")
        if type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive intege
rs")
        if type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive intege
rs")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive intege
rs")
        else:
            self.__position = value

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
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print("#", end='')
                print() 

usr/bin/python3

"""Representing class Square."""


class Square:
    """Continuation from 4-...py in addition with a pub.obj method."""
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        

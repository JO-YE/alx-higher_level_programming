#!/usr/bin/python3

"""Class Rectangle."""


class Rectangle:
    """Defining a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of a Rectangle."""
        return (self.height * self.width)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return((self.height + self.width) * 2)

    def __str__(self):
        """Printing the rectangle with the character #."""
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """This method will return string rep of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Print the message Bye rectangle... when an obj is deleted."""
        print("Bye rectangle...")

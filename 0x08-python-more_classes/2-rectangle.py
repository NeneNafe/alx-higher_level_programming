#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """This initialisez the class Rectangle whic takes arguments like
        width and height"""

        self.width = width
        self.height = height

    def area(self):
        """This returns the area of a rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """This part returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width with the instance value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This part retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets an instance height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

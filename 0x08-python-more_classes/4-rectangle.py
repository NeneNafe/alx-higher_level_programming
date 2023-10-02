#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """This initialisez the class Rectangle whic takes arguments like
        width and height"""

        self.width = width
        self.height = height

    @property
    def width(self):
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

    def area(self):
        """This returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This part returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a new string object from the given object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str


    def __repr__(self):
        """Returns a string representation for recreating the object."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

#!/usr/bin/python3
"""Class Defined"""


class Rectangle:
    """In this, the class has two private instances namely
    width and height"""

    def __init__(self, width=0, height=0):
        """This part initialises theclass with the named instances"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """this instance defines width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This part sets the instance width the argument value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """the width must be an int, therefore, this part check if that is true"""
        if value < 0:
            raise ValueError("width must be >= 0")
        """However, if width tends out to be less than 0, raise the ValueError"""
        self.__width = value

    @property
    def height(self):
        """defines height as an instance to class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """this definition takes the argument value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """Checks whether height is an integer or not"""
        if value < 0:
            raise ValueError("height must be >= 0")
        """if not and int then it prints the valueerror"""
        self.__height = value

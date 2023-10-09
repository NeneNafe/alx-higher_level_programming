#!/usr/bin/python3
# 9-rectangle.py

"""inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """
        initialises the class rectangle with arguments
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Defines the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the representations of a str and print function"""

        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string

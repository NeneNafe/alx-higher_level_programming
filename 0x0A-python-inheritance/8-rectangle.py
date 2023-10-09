#!/usr/bin/python3
"""firsts inherits getgeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    """

    def __init__(self, width, height):
        """
        Initialises clas Rectangle with self, by taking
        width and height as arguments
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

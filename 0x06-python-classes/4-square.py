#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """a class Square that defines a square by: (based on 3-square.py)"""

    def __init__(self, size=0):
        """Initialisez self with size as argument"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the property defined above"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square"""

        return self.__size ** 2

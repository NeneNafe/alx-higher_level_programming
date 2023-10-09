#!/usr/bin/python3
"""Defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""

    def __init__(self, size):
        """
        initialises class square with arugment size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

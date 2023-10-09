#!/usr/bin/python3
"""Defines a class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that is a square"""

    def __init__(self, size):
        """Initialisez the class square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

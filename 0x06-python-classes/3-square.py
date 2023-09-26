#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """This a class Square that defines a square by prev task"""

    def __init__(self, size=0):
        """Initialisez the class square with self and taking size
        as an argument"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """This part checks if size is an int and then prints TypeError,
        if not, ValueError"""

        self.__size = size

    def area(self):
        """Calculates the area of a square"""

        return self.__size ** 2

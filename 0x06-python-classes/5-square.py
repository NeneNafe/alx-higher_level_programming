#!/usr/bin/python3
"""Defines a class sqaure"""


class Square:
    """ a class Square that defines a square by: (based on 4-square.py)"""

    def __init__(self, size=0):
        """This initialises the class square with passing
        argument size with self"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

#!/usr/bin/python3
"""Define class Square"""


class Square:
    """a class that defines a square by the previous example"""

    def __init__(self, size=0):
        """this initializes the class with size as argument
        which is an integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """checks whether size is an int, otherwise typeerror"""

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

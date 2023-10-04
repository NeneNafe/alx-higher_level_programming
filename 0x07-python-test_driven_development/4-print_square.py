#!/usr/bin/python3
"""Defines a print square"""


def print_square(size):
    """This is a function that prints a square with the character #
    and it takse size as an argument, size is the length of the square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)

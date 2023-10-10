#!/usr/bin/python3
"""Defines a function"""


def write_file(filename="", text=""):
    """
    a function that write a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as file:
        NumChar = file.write(text)
        return NumChar

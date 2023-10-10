#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """A function that reads a text file (UTF8)
    and prints it to stdout"""

    with open("my_file_0.txt") as filename:
        for line in filename:
            print(line, end="")

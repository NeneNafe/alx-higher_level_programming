#!/usr/bin/python3
"""Defines a class"""


class MyList(list):
    """
    This is a class called MyList that inherits from list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

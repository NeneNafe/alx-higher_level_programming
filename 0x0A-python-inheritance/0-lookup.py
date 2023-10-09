#!/usr/bin/python3
"""Defines a function"""


def lookup(obj):
    """
    This is a function that return the list of available attributes
    and methods of an object
    """

    return [attr for attr in dir(obj)]

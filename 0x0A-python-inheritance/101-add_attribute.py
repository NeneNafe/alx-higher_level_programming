#!/usr/bin/python3
"""Defines a function"""


def add_attribute(obj, att, value):
    """
    a function that adds a new attribute to an
    object if it’s possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

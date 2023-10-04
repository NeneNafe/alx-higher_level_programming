#!/usr/bin/python3
"""Defines a function"""


def say_my_name(first_name, last_name=""):
    """This is a function that takes two arguments first name and second name
    which must be a string, but if not it will raise a TypeError"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)

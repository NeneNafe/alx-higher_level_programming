#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """
    A class base geometry that as two public instance methods
    """

    def area(self):
        """a public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Another public intance that validates integers"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


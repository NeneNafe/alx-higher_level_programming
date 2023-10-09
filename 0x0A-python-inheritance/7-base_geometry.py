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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

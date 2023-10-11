#!/usr/bin/python3
"""Defines a class"""


class Student:
    """
    This is a class that defines a student by:
    first name, last name, and their age
    """

    def __init__(self, first_name, last_name, age):
        """
        initialises three public instances of class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student"""

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

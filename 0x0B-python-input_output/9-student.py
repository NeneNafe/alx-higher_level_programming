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

    def to_json(self):
        result = {}
        for attr, value in self.__dict__.items():
            result[attr] = self._convert_to_serializable(value)
        return result
    def _convert_to_serializable(self, value):
        if isinstance(value, int) or isinstance(value, bool) or isinstance(value, str):

            return value
        elif isinstance(value, list):
            return [self._convert_to_serializable(item) for item in value]
        elif isinstance(value, dict):
            return {key: self._convert_to_serializable(val) for key, val in value.items()}
        elif hasattr(value, '__dict__'):
            return {key: self._convert_to_serializable(val) for key, val in value.__dict__.items()}
        else:
            return None

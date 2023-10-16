#!/usr/bin/python3
"""Defines a super class Base"""

import json


class Base:

    __nb_objects = 0
    """This is a private class attribute"""

    def __init__(self, id=None):
        """
        Initialisez the class Base by taking arguments like id
        which is initialised to Noe
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

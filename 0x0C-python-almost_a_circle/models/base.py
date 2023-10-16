#!/usr/bin/python3
"""Defines a super class Base"""

import os
import json


class Base:
    """This is a Base Class"""

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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dict = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dict))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        class_name = cls.__name__
        filename = f"{class_name}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            json_str = f.read()

        if json_str:
            list_dicts = cls.from_json_string(json_str)
            instances = [cls.create(**dict_obj) for dict_obj in list_dicts]
            return instances

        return []

#!/usr/bin/python3
"""Defines a super class Base"""


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

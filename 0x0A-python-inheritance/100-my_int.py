#!/usr/bin/python3
"""Deifnes a class"""


class MyInt(int):
    """a class that inherits from int"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        """ responsible for the != operator, to call the parent
        class's __eq__ method (which corresponds to ==)
        with the other object
        """
        return super().__eq__(other)

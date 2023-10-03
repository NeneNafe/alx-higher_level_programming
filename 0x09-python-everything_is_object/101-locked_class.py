#!/usr/bin/python3
"""Define a Class"""


class LockedClass:
    """Defines a locked class that prevents the dynamic creation
    of new intstance attribute, except for an isntance attribute call fistname
    """

    __slots__ = ("first_name")

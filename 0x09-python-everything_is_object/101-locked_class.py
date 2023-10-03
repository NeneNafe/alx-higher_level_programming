#!/usr/bin/pyrhon3
"""Define a Class"""


class LockedClass:
    """Defines a locked class"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                "'LockeClass' object has no attribute '{}'".format(name)
            )
        super().__setattr__(name, value)

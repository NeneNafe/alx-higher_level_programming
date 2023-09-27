#!/usr/bin/python3
"""he Python class MagicClass"""


class MagicClass:
    """creates a magic class that reads bytecode"""

    def __init__(self, radius=0):
        """initialisez the magic class"""

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def are(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi or self.__radius

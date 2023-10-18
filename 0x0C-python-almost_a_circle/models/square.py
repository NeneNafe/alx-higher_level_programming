#!/usr/bin/python3
"""defines a class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialisez the class square with size, x, and y as arguments
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
                f"{self.width}/{self.height}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """an update function that takes args and kwargs as arguments"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns a dictionary representation of a square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

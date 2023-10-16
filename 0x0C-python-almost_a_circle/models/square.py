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

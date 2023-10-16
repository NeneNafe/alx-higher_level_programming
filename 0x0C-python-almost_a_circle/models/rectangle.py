#!/usr/bin/python3
"""Defines a class"""

from models.base import Base


class Rectangle(Base):
    """
    A class rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises the class rectangle with private instance
        attributes, that each has it own public getter & setter
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    def area(self):
        """returns the area of the rectangle instance"""
        return self.width * self.height

        @property
        """retrieves the attribute instance"""
        def width(self):
            return self.__width

        @width.setter
        """a setter method for height"""
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        """a getter method"""
        def height(self):
            return self.__height

        @height.setter
        """a setter method for height"""
        def height(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__height = value

        @property
        """retrieves the attribute instance"""
        def x(self):
            return self.__x

        @x.setter
        """sets value to attribute"""
        def x(self, value):
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        """retrieves the attribute instance"""
        def y(self):
            return self.__y

        @y.setter
        """sets value to attribute"""
        def y(self, value):
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def display(self):
        """displays the rectangls with character #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print()

    def __str__(self):
        """An __str__ function for the class rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assignes an argument to each attribute"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

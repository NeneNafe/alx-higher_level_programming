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

        self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__width * self.__height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def display(self):
        """displays the rectangls with character #"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
                f"{self.__width}/{self.__height}"

    def update(self, *args):
        """Assignes an argument to each attribute"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

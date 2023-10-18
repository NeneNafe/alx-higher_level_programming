#!/usr/bin/python3
# rectangle.py
"""Unittests for Rectangle class"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_width_getter(self):
        obj = Rectangle(10, 15)
        obj.__width = 10
        self.assertEqual(obj.width, 10)

    def test_width_setter(self):
        obj = Rectangle(10, 15)
        # test for ValueError followe by  valid value
        with self.assertRaises(ValueError):
            obj.width = 0
        obj.width = 10  # no exception to be raised
        self.assertEqual(obj.width, 10)

        # Test for TypeError
        with self.assertRaises(TypeError):
            obj.width = "invalid"

        # Test for ValueError
        with self.assertRaises(ValueError):
            obj.width = 0

    def test_height_getter(self):
        obj = Rectangle(5, 10)
        height = obj.height
        self.assertEqual(height, 10)

    def test_area(self):
        obj = Rectangle(6, 8)
        area = obj.area()
        self.assertEqual(area, 6 * 8)

    def test_update(self):
        # Test for arguments
        obj = Rectangle(1, 10, 20, 30, 40)
        obj.update(2, 15, 21, 36, 47)

        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 15)
        self.assertEqual(obj.height, 21)
        self.assertEqual(obj.x, 36)
        self.assertEqual(obj.y, 47)

        # Test for kwargs
        obj = Rectangle(1, 10, 20, 30, 40)
        obj.update(id=2, width=15, height=25, x=35, y=45)

        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.width, 15)
        self.assertEqual(obj.height, 25)
        self.assertEqual(obj.x, 35)
        self.assertEqual(obj.y, 45)

    def test_to_dictionary(self):
        # Test if the dictionary has correct key-value pairs
        obj = Rectangle(1, 10, 20, 30, 40)
        result = obj.to_dictionary()

        self.assertEqual(result["width"], 1)
        self.assertEqual(result["height"], 10)
        self.assertEqual(result["x"], 20)
        self.assertEqual(result["y"], 30)
        self.assertEqual(result["id"], 40)


if __name__ == '__main__':
    unittest.main()

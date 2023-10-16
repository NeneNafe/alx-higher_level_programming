#!/usr/bin/python3
# base.py
"""Unittests for base class"""

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test with an empty list
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        # Test with None
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

        # Test with a non-empty list
        data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        ex_result = ('[{"id": 1, "name": "Item 1"}, '
                     '{"id": 2, "name": "Item 2"}]')
        result = Base.to_json_string(data)
        self.assertEqual(result, ex_result)

    def test_save_to_file(self):
        # Create a list of objects to test with
        rect1 = Rectangle(3, 5)
        rect2 = Rectangle(2, 4)
        list_objs = [rect1, rect2]

        # Calls the function
        Rectangle.save_to_file(list_objs)

        # Reads the grenerated JSON file and verifies it's contents
        class_name = Rectangle.__name__
        filename = f"{class_name}.json"
        self.assertTrue(os.path.exists(filename))

        # rads the content from the file
        with open(filename, 'r') as f:
            json_content = f.read()

    def test_from_json_string(self):
        # Tests with an empty JSON string
        json_string = "[]"
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

        # Test with a None JSON string
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

        # Test with a non-empty JSON string
        json_string = '[{"id": 1, "name": "Item 1"}, '\
            '{"id": 2, "name": "Item 2"}]'
        expected_result = ([{"id": 1, "name": "Item 1"},
                            {"id": 2, "name": "Item 2"}])
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_create(self):
        # Test creating a dummy Rectangle method
        dictionary = {'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0}
        instance = Rectangle.create(**dictionary)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 5)
        self.assertEqual(instance.height, 10)
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)

        # Test creating a dummy square method
        dictionary = {'id': 2, 'size': 7, 'x': 2, 'y': 2}
        instance = Square.create(**dictionary)
        self.assertIsInstance(instance, Square)
        self.assertEqual(instance.id, 2)
        self.assertEqual(instance.size, 7)
        self.assertEqual(instance.x, 2)
        self.assertEqual(instance.y, 2)

    def test_from_json_string(self):
        # Test with  None JSON string
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

        # Test with an empty JSON string
        json_string = []
        result = Base.from_json_string(json_string)
        self.assertEwaula(result, [])

        # Test the validity of a string
        json_string = '[{"id": 1, "name": "Item 1"}, '\
            '{"id": 2, "name": "Item 2"}]'
        expected_result = [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"}
        ]

        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

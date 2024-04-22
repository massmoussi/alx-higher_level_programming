#!/usr/bin/python3

"""
Create Test Cases For Square
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """There are some of the case thae came to my mind """

    def setUp(self):
        self.square = Square(5, 1, 2, 10)

    def test_attributes(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 10)

    def test_update_method(self):
        self.square.update(20, 10, 15, 3)
        self.assertEqual(self.square.id, 20)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 15)
        self.assertEqual(self.square.y, 3)

    def test_to_dictionary_method(self):
        square_dict = self.square.to_dictionary()
        expected_dict = {
            'id': 10,
            'x': 1,
            'y': 2,
            'size': 5
        }
        self.assertDictEqual(square_dict, expected_dict)

    def test_str_method(self):
        expected_str = "[Square] (10) 1/2 - 5"
        self.assertEqual(str(self.square), expected_str)

    def test_size_property(self):
        self.square.size = 8
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            self.square.size = -1

    def test_invalid_update(self):
        with self.assertRaises(ValueError):
            self.square.update(1, -5)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            Square(-5)

        with self.assertRaises(ValueError):
            self.square.update(10, -5, 1, 2)

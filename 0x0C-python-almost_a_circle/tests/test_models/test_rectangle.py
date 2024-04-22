#!/usr/bin/python3

"""
Create Test Cases For rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Below some Test case for rectangle """

    def setUp(self):
        self.rectangle = Rectangle(5, 3, 2, 1, 1)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 15)

    def test_display(self):
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.rectangle.display()

        sys.stdout = sys.__stdout__

        result = captured_output.getvalue().strip()
        expected_output = '#####\n  #####\n  #####'

        self.assertEqual(result, expected_output)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 2/1 - 5/3")

    def test_update(self):
        self.rectangle.update(2, 7, 4, 1, 2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 1/2 - 7/4")

    def test_update_kwargs(self):
        self.rectangle.update(width=6, height=2, id=3)
        self.assertEqual(str(self.rectangle), "[Rectangle] (3) 2/1 - 6/2")

    def test_to_dictionary(self):
        expected_dict = {
                'id': 1,
                'width': 5,
                'height': 3,
                'x': 2,
                'y': 1
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -1

    def test_str_width(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = "text"

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = -1

    def test_str_height(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = "text"

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_str_x(self):
        with self.assertRaises(TypeError):
            self.rectangle.x = "text"

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_str_y(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = "text"

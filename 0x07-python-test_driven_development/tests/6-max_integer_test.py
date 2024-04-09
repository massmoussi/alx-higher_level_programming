#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

"""Test Max_Integer Function using unittest"""


class TestMaxInteger(unittest.TestCase):
    """
    Test various list of dataTypes
    """
    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_normal_list(self):
        self.assertEqual(max_integer([1, 5, 4, 3, 2]), 5)

    def test_float_list(self):
        self.assertEqual(max_integer([15.0, 17.8, 1.5, 4.5]), 17.8)

    def test_negative_list(self):
        self.assertEqual(max_integer([-1, -10, -5, -2]), -1)

    def test_dups_list(self):
        self.assertEqual(max_integer([100, 77, 25, 100, 100]), 100)

    def test_single_list(self):
        self.assertEqual(max_integer([99]), 99)

    def test_char_list(self):
        self.assertEqual(max_integer(["A", "B", "Z"]), "Z")

    def test_text_list(self):
        self.assertEqual(max_integer(["hello", "bye"]), "hello")


if __name__ == '__main__':
    unittest.main()

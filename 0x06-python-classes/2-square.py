#!/usr/bin/python3

"""Class Declaration"""


class Square:
    """Instantiation"""
    def __init__(self, size=0):
        """assigne size to private instance attribute"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

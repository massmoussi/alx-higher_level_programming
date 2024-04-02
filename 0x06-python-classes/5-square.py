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

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print("")
        for j in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

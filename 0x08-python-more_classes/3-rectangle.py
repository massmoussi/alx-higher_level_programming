#!/usr/bin/python3

"""Class Declaration"""


class Rectangle:
    """
    a Class with 2 argument width & height
    Check if the width & height are integer or less than Zero
    Raise TypeError or ValueError
    """

    def __init__(self, width=0, height=0):
        """"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        peri = 0
        if not self.width == 0 and not self.height == 0:
            peri = (self.width + self.height) * 2
        return peri

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for i in range(self.height):
            rec_str += "#" * self.width + "\n"
        return rec_str[:-1]

#!/usr/bin/python3

"""square is an inheretant of Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square is an inheretant from Rectangle
    """
    def __init__(self, size):
        """
        Initialize the inheret Class
        check the size using integer_validator methods
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        classname = str(self.__class__.__name__)
        opr = str(self.__size) + "/" + str(self.__size)
        return "[" + classname + "]" + " " + opr

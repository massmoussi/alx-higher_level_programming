#!/usr/bin/python3

"""Rectangle is an inheretent"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is an inheretant from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize the inheret Class
        use the integer validator methods
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        classname = str(self.__class__.__name__)
        opr = str(self.__width) + "/" + str(self.__height)
        return "[" + classname + "]" + " " + opr

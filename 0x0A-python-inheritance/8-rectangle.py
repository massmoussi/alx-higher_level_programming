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

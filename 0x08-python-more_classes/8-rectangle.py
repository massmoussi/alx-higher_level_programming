#!/usr/bin/python3

"""Class Declaration"""


class Rectangle:
    """
    a Class with 2 argument width & height
    Check if the width & height are integer or less than Zero
    Raise TypeError or ValueError
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if type(self.print_symbol) is str:
            for i in range(self.height):
                rec_str += self.print_symbol * self.width + "\n"
        if isinstance(self.print_symbol, (list, int)):
            for i in range(self.height):
                rec_str += str(self.print_symbol) * self.width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

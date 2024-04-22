#!/usr/bin/python3

"""Define New Class Rectancle Inheret from base """
from models.base import Base


class Rectangle(Base):
    """
    instatiate all rectangle attributes & make them private attribute
    use the super() to get from id value from base
    setup all private attribute Getter & setter one by one
    """

    chars = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        this method is for caluculating the area of
        a rectangle it take width & height then multiply
        them
        """
        return self.height * self.width

    def display(self):
        """
        based on dimension of the rectangle already provided
        the display method print spaces & # symbol
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end='')
            for j in range(self.width):
                print(Rectangle.chars, end='')
            print()

    def __str__(self):
        name = "[Rectangle]"
        id_p = "(" + str(self.id) + ")"
        xy_p = str(self.x) + "/" + str(self.y)
        widh_p = str(self.width) + "/" + str(self.height)
        resu = name + " " + id_p + " " + xy_p + " - " + widh_p
        return resu

    def update(self, *args, **kwargs):
        """
        the update method update the attributes value using args
        it Check the len of args first  in order to put each arg in their
        right place
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionart method simple method
        return dictionary representation
        Take no argument
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }

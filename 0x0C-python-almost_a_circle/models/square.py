#!/usr/bin/python3

"""Define Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inisialize the attributes to 0 or None
    use super() to inherent some attribute property
    use __str__ magic method to display a Good looking output
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = "[Square]"
        v_id = "(" + str(self.id) + ")"
        x_y = str(self.x) + "/" + str(self.y)
        v_size = str(self.size)
        resu = name + " " + v_id + " " + x_y + " " + "-" + " " + v_size
        return resu

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update method is method the update
        object dimension , based on their placement
        by using args we need to get the len of args
        the start put every arg in their right place
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.size = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionary method
        Take string then Convert it to dictionary
        via dictionary text formatting
        """
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.width
            }

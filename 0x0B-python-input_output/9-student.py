#!/usr/bin/python3

"""Define Our Class Student"""


class Student:
    """
    instantiate our Class with
    set public attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        get the data as dictionary
        and convert it to json
        """
        return self.__dict__

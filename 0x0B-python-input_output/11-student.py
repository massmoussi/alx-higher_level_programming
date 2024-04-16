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

    def to_json(self, attrs=None):
        """
        Declare empty json_data var
        Check if the attrs is not None
        check if attrs a list
        iterate over the attrs list check if the attr is str & attr in class
        if it exist we call using getattr
        """
        json_data = {}

        if attrs is not None:
            if isinstance(attrs, list):
                for attr in attrs:
                    if isinstance(attr, str) and hasattr(self, attr):
                        json_data[attr] = getattr(self, attr)
        else:
            json_data = self.__dict__

        return json_data

    def reload_from_json(self, json):
        """
        replaces all attr of the student instances
        """
        return self.__dict__.update(json)

#!/usr/bin/python3

"""Function that check if the object is an of class that inherited"""


def inherits_from(obj, a_class):
    """
    Check if the obj type is inherit of a_class using issubclasse
    Datatypes are class , print(type(9)) you will be shock by the output
    Return True  or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False

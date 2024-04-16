#!/usr/bin/python3

"""Function To check if the object is the same as the instace"""


def is_same_class(obj, a_class):
    """
    Check if the instance is an instance of class
    using isinstance
    isinstance is a function return either True or False
    """
    if type(obj) is a_class:
        return True
    return False

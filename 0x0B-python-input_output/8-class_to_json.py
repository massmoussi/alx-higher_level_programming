#!/usr/bin/python3


""" Define our function & Import all modules needed"""


def class_to_json(obj):
    """
    Class to json function is function that take instance
    of class and convert into json represetation
    we take:
        obj: the instace of the classe
        __dict__ : to be selective & include only object that has
        dictionnary representation
    """
    return obj.__dict__

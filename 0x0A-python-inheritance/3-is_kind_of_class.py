#!/usr/bin/python3

""" Check if the instance is derive from that Class"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance
    or
    an instance of class that inherited from.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3

"""an addition function"""


def add_integer(a, b=98):
    """
    Return the Total

    Check if the argument are int or float
    if the Check valid raise a TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b

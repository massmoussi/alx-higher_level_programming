#!/usr/bin/python3

""" a Function Print Names"""


def say_my_name(first_name, last_name=""):
    """
    Print the Full name or the First name only

    Check the validity of Type first Before Process.
    if the Check is valid raise a TypeError
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

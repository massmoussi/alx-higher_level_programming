#!/usr/bin/python3

"""Function Print Square"""


def print_square(size):
    """
    print squares base on size
    Check if the size is a valid integer
    if it check fail raise a TypeError
    if the size is less than Zero raise a Value Error
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

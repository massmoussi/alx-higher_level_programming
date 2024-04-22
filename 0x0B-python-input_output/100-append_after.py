#!/usr/bin/python3

""" Deine our function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Search for string in each line then
    add new string to file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

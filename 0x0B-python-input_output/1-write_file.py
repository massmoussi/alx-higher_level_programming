#!/usr/bin/python3


""" function to write in file"""


def write_file(filename="", text=""):
    """
    This function open the file or create a new one if it not exist
    using f.write take data from text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

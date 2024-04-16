#!/usr/bin/python3


""" Function append text to to file"""


def append_write(filename="", text=""):
    """
    append text to file , if the file not exist the function Create a new one
    return the number of chars written to the file
    """
    with open(filename, 'a+', encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3


""" function read from a file"""


def read_file(filename=""):
    """
    read_file function , simple function read text from file
    the file is in filename argument
    encoding argument to handle the text format
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")

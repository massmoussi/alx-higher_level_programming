#!/usr/bin/python3
"""Define our function & import modules"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function allow to you to write an Object
    into text file using JSON represetation
    json.dump after we open the file on write mode
    has the ability to write the object in the file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

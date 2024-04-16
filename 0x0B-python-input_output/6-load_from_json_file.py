#!/usr/bin/python3
"""Define our Function & import modules """
import json


def load_from_json_file(filename):
    """
    This Function Open a file which a json
    load all of the json data as object
    """
    with open(filename, 'r') as f:
        return json.load(f)

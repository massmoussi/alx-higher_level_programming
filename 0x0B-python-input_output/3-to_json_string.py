#!/usr/bin/python3
""" Define out to_json_string function"""
import json


def to_json_string(my_obj):
    """
    in this Code we import json library to
    use json dump and print the json representation of the object
    """
    return json.dumps(my_obj)

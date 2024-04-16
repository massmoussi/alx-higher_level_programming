#!/usr/bin/python3
"""Defining our function & their library """
import json


def from_json_string(my_str):
    """
    in This take we take string as argument,not same as
    the "to_json_string"
    """
    return json.loads(my_str)

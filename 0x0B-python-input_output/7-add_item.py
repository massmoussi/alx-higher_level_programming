#!/usr/bin/python3

"""Define our function & Import all the modules we need"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """
    function to load from json file
    and append to that json file base on our suppy args
    then convert the content of the file json
    """
    filename = "add_item.json"
    try:
        jsonfile = load_from_json_file(filename)
    except FileNotFoundError:
        jsonfile = []
    for arg in range(1, len(args)):
        jsonfile.append(args[arg])
    save_to_json_file(jsonfile, filename)


if __name__ == "__main__":
    add_item(sys.argv)

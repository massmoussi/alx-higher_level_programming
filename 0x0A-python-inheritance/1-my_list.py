#!/usr/bin/python3

""" Inheret list to MyList"""


class MyList(list):
    """
    sort a list of int using sorted function
    also via inheretance Concept
    """

    def print_sorted(self):
        sort_list = sorted(self)
        print(sort_list)

#!/usr/bin/python3

""" Funct t find a Peak in List of Ints"""


def find_peak(list_of_integers):
    """
    Find the Peaks within the list of unsorted Integer

    Args:
        list_of_integers (list): A list of unsorted Integers

    Returns:
        int or None
    """
    if not list_of_integers:
        return None
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]

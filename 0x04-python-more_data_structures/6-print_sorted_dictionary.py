#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dicc = list(a_dictionary)
    new_dicc.sort()
    for key in new_dicc:
        print("{}: {}".format(key, a_dictionary[key]))

#!/usr/bin/python3
def no_c(my_string):
    ctoremove = "cC"
    new_string = ''.join(char for char in my_string if char != ctoremove)
    return new_string

#!/usr/bin/python3
def no_c(my_string):
    ctoremove = "c"
    my_string = ''.join(char for char in my_string if char != ctoremove)
    return my_string

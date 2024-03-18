#!/usr/bin/python3
def no_c(my_string):
    ctoremove = "c"
    ctomove = "C"
    new_string = ''.join(char for char in my_string
                         if char != ctoremove and char != ctomove)
    return new_string

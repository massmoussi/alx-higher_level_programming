#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_set = set(my_list)
    rs = 0
    for element in n_set:
        rs += element
    return rs

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for b in i:
            print("{}".format(b), end='')
        print()

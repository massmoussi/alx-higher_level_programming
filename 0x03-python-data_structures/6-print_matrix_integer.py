#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for b, element in enumerate(row):
            print("{}".format(element), end="")
            if b != len(row) -1:
                print("", end="")
        print()

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    w_matrix = []
    for row in matrix:
        w_row = []
        for i in row:
            w_row.append(i ** 2)
        w_matrix.append(w_row)
    return w_matrix

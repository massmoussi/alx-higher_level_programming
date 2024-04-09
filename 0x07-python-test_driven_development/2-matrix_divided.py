#!/usr/bin/python3
"""Calculate Division of matrix , Store results into New matrix"""


def matrix_divided(matrix, div):
    """
    Return the new_matrix contain the division results
    Check  each row & each element if they are int or float
    Check if the rows has similar length
    Check if the Divison is 0
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix

#!/usr/bin/python3
"""Defining Our FUnction"""


def pascal_triangle(n):
    """
    one of the hardest Task I ever Face
    Need some Math Skills & calculation
    However Thanks for Community to help me Under
    stand the pascal triangle Concept
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

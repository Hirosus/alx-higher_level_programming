#!/usr/bin/python3
"""
This module defines a function for generating Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.

    :param n: The number of rows for Pascal's triangle.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


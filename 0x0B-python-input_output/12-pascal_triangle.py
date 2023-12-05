#!/usr/bin/python3

def pascal_triangle(n):
    """Generates Pascal's triangle up to the specified level.

    Args:
        n (int): The level of Pascal's triangle.

    Returns:
        list of lists: A list of lists of integers representing Pascal's triangle.
                       Returns an empty list if n <= 0.
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

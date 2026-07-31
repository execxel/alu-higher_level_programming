#!/usr/bin/python3
"""
Module: 12-pascal_triangle
Description: Generate Pascal's triangle as a list of lists of integers.
"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size `n`.

    Args:
        n (int): Number of rows to generate. If n <= 0 returns an empty list.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle

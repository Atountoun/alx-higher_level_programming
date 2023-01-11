#!/usr/bin/python3
"""A module for pascal's triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n;

    Args:
        n (int): the base of the triangle
    Return:
        Empty list: if n <= 0
        List of lists: if n > 0
    """
    result = []
    for i in range(i):
        row = []
        for k in range(i + 1):
            if k == 0 or k == i:
                row.append(1)
            else:
                high = result[i-1]
                row.append(high[j-1] + high[j])
        result.append(row)
    return result

#!/usr/bin/python3
"""A module that contains a single method about matrix."""


def matrix_divided(matrix, div):
    """A division operation of elements of a matrix.

    Args:
        matrix: (list(list)): the matrix to be used
        div: (int, float): the divider

    Returns:
        A new matrix with each element divided by div rounded to 2
        decimal places.

    Raises:
        TypeError:
            if matrix is not a `list of list` of integers/floats
            if each row of the matrix don't have the same size
            if div is not a number( integer of float)
        ZeroDivisionError:
            if div is equal to 0
    """

    for ele in matrix:
        if not isinstance(ele, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            for value in ele:
                if not isinstance(value, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(ele) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for ele in matrix:
        new_matrix.append([round(value/div, 2) for value in ele])

    return new_matrix

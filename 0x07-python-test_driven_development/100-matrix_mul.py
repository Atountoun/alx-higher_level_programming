#!/usr/bin/python3
"""A module for multiplication of two matrix."""


def matrix_mul(m_a, m_b):
    """Function to multiply two matrix.

    Args:
        m_a (list of lists): the first matrix
        m_b (list of lists): the second matrix

    Returns:
        m_a * m_b (list of lists): the result of the multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all((isinstance(el, list) for el in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not all((isinstance(el, list) for el in m_b)):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    for el in m_a:
        for value in el:
            if type(value) is not int and type(value) is not float:
                raise ValueError("m_a should contain only integers or floats")

    for el in m_b:
        for value in el:
            if type(value) is not int and type(value) is not float:
                raise ValueError("m_b should contain only integers or floats")

    if not all([len(m_a[0]) == len(next_ele) for next_ele in m_a]):
        raise TypeError("each row of m_a must be of the same size")

    if not all([len(m_b[0]) == len(next_ele) for next_ele in m_b]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for i in range(len(m_a)):
        row = [0] * len(m_b[0])
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                row[j] += m_a[i][k] * m_b[k][j]
        res.append(row)

    return res

#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    len_ta = len(tuple_a)
    len_tb = len(tuple_b)
    len_min_tu = len_ta if len_ta < len_tb else len_tb
    max_tu = tuple_a if len_ta > len_tb else tuple_b
    result = []

    for i in range(len_min_tu):
        result.append(tuple_a[i] + tuple_b[i])

    for i in max_tu[len_min_tu:]:
        result.append(i)

    return tuple(result)

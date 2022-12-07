#!/usr/bin/python3

def common_elements(set_1, set_2):
    com_set = set()
    for el in set_1:
        if el in set_2:
            com_set.add(el)

    return (com_set)

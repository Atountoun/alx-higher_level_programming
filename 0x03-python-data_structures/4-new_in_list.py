#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    b = my_list[:]
    if idx < len(my_list) and idx > -1:
        b[idx] = element

    return (b)

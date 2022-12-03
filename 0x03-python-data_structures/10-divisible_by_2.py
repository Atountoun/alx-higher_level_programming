#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    is_div_by_2 = []
    for x in my_list:
        is_div_by_2.append(x % 2 == 0)

    return (is_div_by_2)

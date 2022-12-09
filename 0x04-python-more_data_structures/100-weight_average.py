#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    y_sum = sum([i[1] for i in my_list])
    x_y_product = sum([i[0] * i[1] for i in my_list])

    return (x_y_product / y_sum)

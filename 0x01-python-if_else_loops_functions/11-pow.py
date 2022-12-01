#!/usr/bin/python3

def pow(a, b):
    exp = b if (b > 0) else -b
    result = 1
    for i in range(exp):
        result *= a
    if b < 0:
        return 1 / result
    return result

#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in ops.keys():
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    a = sys.argv[1]
    b = sys.argv[3]
    op = sys.argv[2]

    print(f"{a} {op} {b} = {ops.get(op)(int(a), int(b))}")

#!/usr/bin/python3

import sys

if __name__ == "__main__":

    countArgs = len(sys.argv)
    result = 0

    for i in range(1, countArgs):
        result += int(sys.argv[i])

    print(result)

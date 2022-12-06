#!/usr/bin/python3

import sys

if __name__ == "__main__":

    argsCount = len(sys.argv) - 1
    if argsCount == 0:
        print(f"{0} arguments.")
    elif argsCount == 1:
        print(f"{1} argument:")
        print(f"{1}: {sys.argv[1]}")
    else:
        print(f"{argsCount} arguments:")
        if argsCount:
            for i in range(1, argsCount + 1):
                print(f"{i}: {sys.argv[i]}")

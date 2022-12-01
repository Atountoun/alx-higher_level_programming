#!/usr/bin/python3

def print_last_digit(number):
    number = -number if (number < 0) else number
    lastD = number % 10
    print(lastD, end="")
    return lastD

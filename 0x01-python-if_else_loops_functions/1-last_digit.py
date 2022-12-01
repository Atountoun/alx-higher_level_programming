#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

if lastDigit > 5:
    pos = "greater than 5"
elif lastDigit == 0:
    pos = "0"
elif lastDigit < 6:
    pos = "less than 6 and not 0"

print(f"Last digit of {number} is {lastDigit} and is {pos}")

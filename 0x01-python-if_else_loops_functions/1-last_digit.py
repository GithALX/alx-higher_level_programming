#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "and is less than 6 and not 0"
if number < 0:
    num = -number
    n_rem = num % 10
rem = number % 10
if rem == 0:
    print(f"Last digit of {number:d} is {rem:d} and is {0}")
elif rem > 5:
    if number < 0:
        print(f"Last digit of {number:d} is -{n_rem:d} {s}")
    else:
        print(f"Last digit of {number:d} is {rem:d} and is greater than {5}")
elif rem < 6:
    if number < 0:
        print(f"Last digit of {number:d} is -{n_rem:d} {s}")
    else:
        print(f"Last digit of {number:d} is {rem:d} {s}")

#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
print(
        "Last digit of {:d} is {:d} and is "
        .format

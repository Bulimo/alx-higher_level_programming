#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
else:
    num = number
n = num % 10
if n == 0:
    s1 = "and is 0"
elif n > 5:
    s1 = "and is greater than 5"
else:
    s1 = "and is less than 6 and not 0"
if number < 0:
    n = n * -1
print(f"Last digit of {number:d} is {n:d} {s1}")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if 10 > number > -10:
    lastd = number
else:
    lastd = number % 10
if lastd > 5:
    n = "greater than 5"
    print("Last digit of {:n} is {:n} and is {:s}".format(number, lastd, n))
elif lastd == 0:
    print("Last digit of {:n} is {:n} and is 0".format(number, lastd))
elif lastd < 6:
    n = "less than 6 and not 0"
    print("Last digit of {:n} is {:n} and is {:s}".format(number, lastd, n))

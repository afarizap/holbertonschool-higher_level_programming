#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberabs = abs(number)
if numberabs < 10:
    lastdigit = numberabs
else:
    lastdigit = numberabs % 10

print("Last digit of {} is {} and is ".format(number, lastdigit), end = "")
if lastdigit > 5:
    print("greater than 5")
elif lastdigit == 0:
    print("0")
elif lastdigit < 6:
    print("less than 6 and not 0")
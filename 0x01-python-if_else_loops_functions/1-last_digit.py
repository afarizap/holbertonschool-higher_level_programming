#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(str(number)[-1:])
if number < 0:
    slastd = lastd * -1
else:
    slastd = lastd
print("Last digit of {} is {} and is ".format(number, slastd), end="")
if lastd > 5:
    print("greater than 5")
elif lastd == 0:
    print("0")
else:
    print("less than 6 and not 0")

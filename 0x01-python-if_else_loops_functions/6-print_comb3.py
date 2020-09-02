#!/usr/bin/python3
for x in range(0, 8):
    for y in range(1, 10):
        if y > x:
            print("{}{}, ".format(x, y), end="")
print("89")

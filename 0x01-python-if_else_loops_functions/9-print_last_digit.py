#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    lastnumber = number % 10
    print("{}".format(lastnumber), end="")
    return lastnumber

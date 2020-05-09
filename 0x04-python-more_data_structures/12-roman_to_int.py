#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman2 = reversed(roman_string)
        new = 0
        new2 = 0
        for i in roman2:
            if rom[i] >= new2:
                new = new + rom[i]
            elif rom[i] < new2:
                new = new - rom[i]
            new2 = rom[i]
        return new
    else:
        return 0

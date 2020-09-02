#!/usr/bin/python3
def remove_char_at(str, n):
    if n > -1:
        new_str = str[:n] + str[n+1:]
        return new_str
    return str

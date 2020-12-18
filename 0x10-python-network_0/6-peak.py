#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    l = list_of_integers
    if not l:
        return None
    if len(l) == 1:
        return l[0]
    left = l[0]
    for i in l:
        right = i
        if left > right:
            return left
        if left < right:
            left = right
    return left

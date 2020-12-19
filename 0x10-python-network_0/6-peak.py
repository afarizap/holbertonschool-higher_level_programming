#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    if list_of_integers:
        return max(list_of_integers)
    return None

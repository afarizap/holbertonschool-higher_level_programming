#!/usr/bin/python3
"""
matrix division operation
"""


def matrix_divided(matrix, div):
    """
    divides each number in a matrix by a number (div)
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    len1 = len(matrix[0])

    for i in matrix:
        if type(i) is not list or type(matrix) is not list:
            raise TypeError(err1)
        if len(i) != len1:
            raise TypeError(err2)
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(err1)
    if type(div) not in [int, float]:
        raise TypeError(err3)
    if div is 0:
        raise ZeroDivisionError(err4)
    new = [[round((j / div), 2) for j in i] for i in matrix]
    return new

if __name__ == "__main__":
    import doctest

    doctest.testfile("./tests/2-matrix_divided.txt")

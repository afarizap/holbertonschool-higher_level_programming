#!/usr/bin/python3
def matrix_divided(matrix, div):
    mtrxerr = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is in [int, float, list]:
        pass
    else:
        raise TypeError(mtrxerr)
    new = [[j / div for j in i] for i in matrix]
    return new

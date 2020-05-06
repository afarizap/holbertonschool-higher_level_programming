#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    R = len(matrix)
    for i in range(R):
        print(*matrix[i])

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = [[0 for _ in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res[i][j] = matrix[i][j] ** 2
    return res

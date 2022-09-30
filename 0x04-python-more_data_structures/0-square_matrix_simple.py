#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #new_matrix = []
   # m  = [x * x for x in new_matrix]
    m = lambda x: x**2
    new = list(map(m, matrix))
    return new

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)


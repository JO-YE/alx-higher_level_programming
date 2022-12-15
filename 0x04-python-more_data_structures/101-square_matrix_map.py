#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
# Note we are dealing with 2 dimentional 

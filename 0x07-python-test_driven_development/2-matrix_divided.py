#!/usr/bin/python3

'''This module contain function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''Function that divide all elements of a matrix.'''
    if type(div) is not int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    for row in matrix:
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')
    return list(map(lambda row: list(map(lambda num: round(num / div, 2),\
 row)),matrix.copy()))
#The round function round it up to whatever decimal point needed.
#In this case, 2 decimal places

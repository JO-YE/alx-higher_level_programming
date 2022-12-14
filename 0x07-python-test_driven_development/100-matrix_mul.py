#!/usr/bin/python3

'''A module that multiply two values.'''


def matrix_mul(m_a, m_b):
    '''Multiplication of two matrix.'''

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if type(m_b) != list:
        raise TypeError('m_b must be a list')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) != list:
            raise TypeError('m_a must be a list of lists')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError('m_b should contain only integers or floats')
        if len(row) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res

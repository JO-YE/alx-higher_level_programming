#!/usr/bin/python3

'''Module contain fxn that multipy matrix using NumPy.'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''A function that multiply 2 matrices.'''
    return np.matmul(m_a, m_b)

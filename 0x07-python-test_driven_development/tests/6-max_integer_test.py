#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Test different scenerios.'''

    def test_end(self):
        my_list = [2, 5, 3, 9]
        self.assertEqual(max_integer(my_list), 9)

    def test_beginning(self):
        '''Test for max at the end.'''
        my_list = [9, 2, 5, 3, 8]
        self.assertEqual(max_integer(my_list), 9)

    def test_middle(self):
        '''Test for max in middle.'''
        my_list = [2, 5, 9, 3, 8]
        self.assertEqual(max_integer(my_list), 9)

    def test_one_negative(self):
        '''One negative exist.'''
        my_list = [2, 5, 9, -3, 8]
        self.assertEqual(max_integer(my_list), 9)

    def test_all_negative(self):
        '''One negative exist.'''
        my_list = [-2, -5, -9, -3, -8]
        self.assertEqual(max_integer(my_list), -2)

    def test_one_element(self):
        '''List of one element.'''
        my_list = [-2]
        self.assertEqual(max_integer(my_list), -2)

    def test_empty_list(self):
        '''Empty list.'''
        my_list = []
        self.assertEqual(max_integer(my_list), None)

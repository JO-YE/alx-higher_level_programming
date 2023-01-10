#!/usr/bin/python3

'''Module that define a Class student.'''


class Student:
    '''This clas define a student.'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return (self.__dict__)

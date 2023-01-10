#!/usr/bin/python3

'''Module that define a Class student.'''


class Student:
    '''This clas define a student.'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for string in attrs:
                if isinstance (string, str):
                    return self.attrs.__dict__
        else:
            return (self.__dict__)

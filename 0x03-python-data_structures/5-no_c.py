#!/usr/bin/python3
"""Function that removes all characters c and C from a string."""


def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str += i
    return (new_str)

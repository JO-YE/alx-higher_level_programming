#!/usr/bin/python3
"""Function that retrieves an element from a list like in C."""


def element_at(my_list, idx):
    if idx < 0:
        return(None)
    if idx > (len(my_list) - 1):# -1 because index counts from 0
        return(None)
    return(my_list[idx])

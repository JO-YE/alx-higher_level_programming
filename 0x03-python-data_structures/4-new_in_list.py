#!/usr/bin/python3
"""Function that replaces an element in a list."""


def new_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    if idx > (len(my_list) -1):
        return(my_list)
    my_new_list = my_list[:]
    my_new_list[idx] = element
    return(my_new_list[:])
    return(my_list)

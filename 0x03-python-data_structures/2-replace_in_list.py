#!/usr/bin/python3
"""Function that replaces an element of a list at a specific position."""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)

    index = (len(my_list) - 1)

    if idx > index:
        return(my_list)

    my_list[idx] = element # assigning the new element for the chosen inde
    
    return(my_list[:])

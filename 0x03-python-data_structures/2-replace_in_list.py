#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)

    index = (len(my_list) - 1)

    if idx > index:
        return(my_list)

    my_list[idx] = element
    
    return(my_list)

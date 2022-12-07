#!/usr/bin/python3
def max_integer(my_list=[]):
    lent = len(my_list)
    if lent == 0:
        return None
    maxi = my_list[0]
    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi

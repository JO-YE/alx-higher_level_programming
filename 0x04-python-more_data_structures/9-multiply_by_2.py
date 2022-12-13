#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for value in a_dictionary.keys():
        new_dic[value] *= 2
    return new_dic

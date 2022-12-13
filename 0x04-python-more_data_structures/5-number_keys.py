#!/usr/bin/python3
def number_keys(a_dictionary):
    total_keys = 0
    key_list = list(a_dictionary.keys())
    for key in key_list:
        total_keys += 1
    return total_keys

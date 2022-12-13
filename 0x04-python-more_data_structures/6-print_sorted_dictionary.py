#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = list(sorted(a_dictionary))
    for i in sort: 
        print("{}: {}".format(i, a_dictionary[i]))

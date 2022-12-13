#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        num = 0
        string = ""
        for value in a_dictionary.keys():
            if a_dictionary[value] > num:
                num = a_dictionary[value]
                string = value
        return string

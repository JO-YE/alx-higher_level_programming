#!/usr/bin/python3
"""Function that checks for lowercasecharacters."""


def islower(c):
    letter = 97
    letter2 = 122
    if c >= chr(letter) and c <= chr(letter2):
        return True
    else:
        return False

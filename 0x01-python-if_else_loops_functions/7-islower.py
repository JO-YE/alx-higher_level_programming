#!/usr/bin/python3
"""Function that checks for lowercasecharacters.""" 
def islower(c):
    letter = 97
    letter2 = 122
# is the letter within a to z(lower)
    if c >= chr(letter) and c <= chr(letter2):
# if yes return true and false otherwise
        return True
    else:
        return False

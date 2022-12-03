#!/usr/bin/python3
"""Print the last digit of a number."""
def print_last_digit(number):
    print(abs(number) % 10, end='')
# absnumber % 10 is used to get last digit
    return(abs(number) % 10)

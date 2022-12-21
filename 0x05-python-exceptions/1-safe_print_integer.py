#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
        print('{:d}'.format(value))
    except:
        return False
    else:
        return True

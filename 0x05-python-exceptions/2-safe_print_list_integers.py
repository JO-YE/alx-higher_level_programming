#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0

    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
    except(TypeError, ValueError):
        pass
    else:
        total += 1

    print()
    return total

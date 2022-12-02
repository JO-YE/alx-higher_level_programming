#!/usr/bin/python3
"""Print the result of the addition of all argument."""
if __name__ == "__main__":
    from sys import argv
    sum = 0
    a = range(len(argv) - 1)
    for i in a:
        sum += int(argv[i + 1])
    print("{}".format(sum))

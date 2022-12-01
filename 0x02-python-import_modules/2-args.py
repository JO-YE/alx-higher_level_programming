#!/usr/bin/python3
"""Print the number of and list of arguments."""
if __name__ == "__main__":
    from sys import argv
i = len(argv) - 1 
# used -1 to reduce the lenght of arg by 1.
# if the actual len is 2 it will count the agr as 1
# this was done to get the result invthe task
if i == 0:
    print("{} {}.".format(i, 'argument'))
else:
    print("{} {}:".format(i, 'arguments'))
if i >= 1:
  for a in range(i):
    print("{}: {}".format(a + 1, argv[a + 1]))
# the plus one will make it print the desired result

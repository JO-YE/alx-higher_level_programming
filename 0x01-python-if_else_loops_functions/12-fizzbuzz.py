#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        fi = num % 3
        bu = num % 5
        if fi == 0 and bu == 0:
            print("{} ".format("FizzBuzz"), end='')
        elif bu == 0:
            print("{} ".format("Buzz"), end='')
        elif fi == 0:
            print("Fizz ", end='')
        else:
            print("{} ".format(num), end='')

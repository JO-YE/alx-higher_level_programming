#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
strg = "Last digit of {} is {} and is {}"
greater = "and is greater than 5"
equals = "and is 0"
less = "and is less than 6 and not 0"
if number < 0:
    digit = -digit
if digit > 5:
    print(strg.format(number, digit, greater))
elif digit == 0:
    print(strg.format(number, digit, equals))
else:
    print(strg.format(number, digit, less))

#!/usr/bin/pyhton3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (not roman_string):
        return 0
    else:
        roman_value = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,\
    'C' : 100, 'D' : 500, 'M' : 1000}
        special_cases = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90,\
    'CD' : 400, 'CM' : 900}
        total = 0
        index = 0
        while index < len(roman_string):
            if roman_string[index: index + 2] in special_cases:
                total += special_cases[roman_string[index: index + 2]]
                index += 2
            else:
                if roman_string[index] in roman_value:
                    total += roman_value[roman_string[index]]
                    index += 1
        return total

#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = 0
    last = 0
    for char in reversed(roman_string):
        val = rom.get(char, 0)
        if val < last:
            num -= val
        else:
            num += val
        last = val

    return num

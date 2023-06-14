#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None

    rmn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string[0] in rmn:
        num = 0
        prev = rmn[roman_string[0]]
    else:
        return None

    for i in roman_string:
        if i not in rmn:
            return None
        if rmn[i] <= prev:
            num = num + rmn[i]
        else:
            num = num + rmn[i] - (2 * prev)
        prev = rmn[i]
    return num

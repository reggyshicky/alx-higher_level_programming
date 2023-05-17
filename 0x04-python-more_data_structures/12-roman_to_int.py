#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    Rom_numeral = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    solution = 0
    valueprev = 0

    for _numeral in reversed(roman_string):
        present_val = Rom_numeral.get(_numeral, 0)  # zero !key

        if present_val >= valueprev:
            solution = solution + present_val
        else:
            solution = solution - present_val
        valueprev = present_val
    return solution

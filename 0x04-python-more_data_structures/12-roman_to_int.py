#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    t = 0
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for r in reversed(roman_string):
        n = d[r]
        t += n if t < n * 5 else -n
    return (t)

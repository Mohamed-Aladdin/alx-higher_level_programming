#!/usr/bin/python3
def magic_calculation(a, b):
    value = 0

    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            else:
                value += (a ** b) / x
        except Exception:
            value = a + b
            break

    return value

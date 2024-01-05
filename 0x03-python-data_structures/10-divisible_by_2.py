#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    temp = []

    for n in my_list:
        temp += ([True] if not n % 2 else [False])

    return (temp)

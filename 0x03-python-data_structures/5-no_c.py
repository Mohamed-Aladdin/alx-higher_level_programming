#!/usr/bin/python3
def no_c(my_string):
    temp = ""
    for letter in my_string:
        if letter != 'C' and letter != 'c':
            temp += letter
    return (temp)

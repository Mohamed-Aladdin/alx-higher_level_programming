#!/usr/bin/python3
for x in range(9):
    for y in range(x, 10):
        print("{}{}".format(x, y), end="\n" if x == 8 and y == 9 else ", ")

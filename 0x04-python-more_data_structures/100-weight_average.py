#!/usr/bin/python3
def weight_average(my_list=[]):
    score = sum([i[0] * i[1] for i in my_list])
    weight = (sum([i[1] for i in my_list]) or 1)
    return (score / weight)

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub in matrix:
        if len(sub) > 0:
            for i in range(len(sub)):
                print("{}".format(sub[i]),
                      end="\n" if i is len(sub) - 1 else " ")
        else:
            print()

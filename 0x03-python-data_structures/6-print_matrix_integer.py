#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub in matrix:
        if len(sub) == 0:
            print()

        for i in range(len(sub)):
            print("{:d}".format(sub[i]),
                  end="\n" if i is len(sub) - 1 else " ")

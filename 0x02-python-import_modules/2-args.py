#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """prints the number of arguments and
    the list of its arguments
    """
    list_var = sys.argv
    len_var = len(list_var) - 1

    if len_var == 0:
        print(len_var, "arguments.")
    elif len_var == 1:
        print(len_var, "argument:")
        for z in range(1, len_var + 1):
            print("{:d}: {}".format(z, list_var[z]))
    elif len_var > 1:
        print(len_var, "arguments:")
        for k in range(1, len_var + 1):
            print("{:d}: {}".format(k, list_var[k]))

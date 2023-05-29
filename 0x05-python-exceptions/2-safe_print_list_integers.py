#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_no_of_elems = 0
    for w in range(x):
        try:
            print("{:d}".format(my_list[w]), end="")
            real_no_of_elems += 1
        except(ValueError, TypeError):
            pass
    print()
    return real_no_of_elems

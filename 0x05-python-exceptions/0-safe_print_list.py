#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for w in range(x):
            print(my_list[w], end="")
    except IndexError:
        x = w
    finally:
        print()
        return x

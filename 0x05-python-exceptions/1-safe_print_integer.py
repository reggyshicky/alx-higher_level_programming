#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value >= 0 or value < 0:
            print("{:d}".format(value))
            digit_it_is = True
    except Exception:
        digit_it_is = False
    return digit_it_is

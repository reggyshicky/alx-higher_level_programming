#!/usr/bin/python3
def print_last_digit(number):
    L_digit = abs(number) % 10
    print(L_digit, end="")
    return L_digit

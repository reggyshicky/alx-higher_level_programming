#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = (sys.argv[2])
    b = int(sys.argv[3])

    if operator == "+":
        solution = add(a, b)
    elif operator == "-":
        solution = sub(a, b)
    elif operator == "*":
        solution = mul(a, b)
    elif operator == "/":
        solution = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, solution))

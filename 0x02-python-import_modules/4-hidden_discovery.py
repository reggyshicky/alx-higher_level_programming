#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    for majina in sorted(dir(hidden_4)):
        if not majina.startswith('__'):
            print(majina)

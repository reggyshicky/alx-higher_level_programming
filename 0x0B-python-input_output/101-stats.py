#!/usr/bin/python3
"""
Module documentation for a script that reads stdin
line by line and computes metrics
"""


from sys import stdin


status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_size = i = 0


def print_status():
    """function that computes metrics"""
    print(f'File size: {total_size}')
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))


try:
    for line in stdin:
        split_line = line.split()
        if len(split_line) >= 2:
            status = split_line[-2]
            total_size += int(split_line[-1])
            if status in status_codes:
                status_codes[status] += 1
        w = w + 1

        if w % 10 == 0:
            print_status()
    print_status()
except KeyboardInterrupt as e:
    print_status()

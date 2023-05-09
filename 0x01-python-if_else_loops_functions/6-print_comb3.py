#!/usr/bin/python3
for z in range(0, 10):
    for w in range(z+1, 10):
        print("{:d}".format(z), end='')
        if z == 8 and w == 9:
            print("{:d}".format(w), end='\n')
        else:
            print("{:d}".format(w), end=', ')

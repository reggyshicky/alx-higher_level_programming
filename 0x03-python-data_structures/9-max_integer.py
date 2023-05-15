#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Int_Max = my_list[0]
    for h in my_list:
        if h > Int_Max:
            Int_Max = h
    return Int_Max

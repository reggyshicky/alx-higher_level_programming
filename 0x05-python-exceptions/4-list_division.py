#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    our_newlist = []

    for w in range(list_length):
        try:
            our_newlist.append(my_list_1[w] / my_list_2[w])
        except ZeroDivisionError:
            our_newlist.append(0)
            print("division by 0")
            continue
        except IndexError:
            our_newlist.append(0)
            print("out of range")
            continue
        except TypeError:
            our_newlist.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return our_newlist

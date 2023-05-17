#!/usr/bin/python3
def search_replace(my_List, search, replace):
    solution = list(my_List)
    for w in range(len(solution)):
        if solution[w] == search:
            solution[w] = replace
    return solution

#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = set((my_list))
    j = 0
    for i in add:
        j += i
    return (j)

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    c_list = my_list.copy()
    if idx < 0:
        return c_list
    if idx > len(c_list):
        return c_list
    else:
        c_list[idx] = element
        return(c_list)

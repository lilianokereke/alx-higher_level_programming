#!/usr/bin/python3
def element_at(my_list, idx):
    elem = " "
    if idx < 0:
        return ("None")
    elif idx > len(my_list):
        return ("None")
    else:
        elem += ("{}".format(my_list[idx]))
        return elem

#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if my_string == (""):
        return
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_str += i
    return new_str

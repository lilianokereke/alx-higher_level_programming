#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if my_string == (""):
        return None
    for i in my_string:
        if i is not 'c' and i is not 'C':
            continue
        new_str += i
    return new_str

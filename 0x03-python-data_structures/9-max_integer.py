#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    curr = 0
    if my_list == []:
        return None
    elif len(my_list) == 1:
        largest = my_list[0]
    else:
        curr = my_list[0]
        idx = 1
        for num in my_list:
            if curr < num:
                curr = num
            else:
                curr > num
                curr = curr
        largest = curr
    return largest

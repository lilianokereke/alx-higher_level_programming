#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        new_str+= i
    return new_str

p = "lili ic Coming"
print(no_c(p))
print(no_c("abcd"))
print(no_c("12cvy iklcm i"))

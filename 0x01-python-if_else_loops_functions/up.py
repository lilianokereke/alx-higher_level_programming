#!/usr/bin/python3
def check_upper(ch):
        n_ch = ord(ch)
        if n_ch >= 65 and n_ch <= 96:
            return(n_ch)
        else:
            return(n_ch - 32)

def uppercase(str):
    st = ""
    for ch in str:
        print("{:c}".format(check_upper(ch)), end = "", sep = "' '")

#!/usr/bin/python3
def multiple_returns(sentence):
    length, first = len(sentence), sentence[0]
    new_tup = (length, first,)
    for i in new_tup:
        print(i, end="")
#    print(type(tup))
 #   return new_tup

s = "lilian is a girl"
leng, fir = multiple_returns(s)
print("Length: {:d} - First character: {}".format(len(leng, fir)))

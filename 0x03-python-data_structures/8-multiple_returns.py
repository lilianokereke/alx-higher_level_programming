#!/usr/bin/python3
def multiple_returns(sentence):
    new_tup = ""
    tup = (("Length: {:d} - First character: {}".format(len(sentence, sentence[0])))
    for i in tup:
        print(i, end="")
    print(type(tup))
    return new_tup

print(multiple_returns("lilian is a girl"))

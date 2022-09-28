#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    operator = ['+', '-', '*', '/']

    b =  int(argv[3])
    a = int(argv[1])
#    argv[2] = args
    if len(argv) < 4 or len(argv) > 4:
        print("Usage: /100-my_calculator.py", argv[1], argv[2], argv[3])
        exit(1)
    if argv not in operator:
       print("Unknown operator. Available operators: +, -, *, and /")
       exit (1)
    if argv[2] == '+' :
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-' :
        print("{} {} = {}".format(sub(a, b)))
    elif argv[2] == '*' :
        print(argv[1], operator[2], argv[3], "= {}".format(mul(a, b)))
    elif argv[2] == '/' :
        print(argv[1], operator[3], argv[3], "= {}".format(div(a, b)))

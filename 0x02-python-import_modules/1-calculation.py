#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5


    print(a, " + ", b, "=", calc.add(a,b))
    print(a, " - ", b, "=", calc.sub(a,b))
    print(a, " * ", b, "=", calc.mul(a,b))
    print(a, " / ", b, "=", int(calc.div(a,b)))

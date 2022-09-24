#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b < 2):
        if tuple_a == () or tuple_b == ():
            tuple_a + (0, 0,)
        elif len(tuple_a) == 1:
            turple_a + (0,)
    if len(tuple_a) > 2:
        new_tup = sum(tuple_a[0], tuple_b[0], sum(tuple_a[1], tuple_b[1])
    return new_tup


tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

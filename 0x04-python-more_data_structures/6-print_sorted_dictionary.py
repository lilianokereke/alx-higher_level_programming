#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor = sorted(a_dictionary)
    print (sor, get.values(sor))
    return sor

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)


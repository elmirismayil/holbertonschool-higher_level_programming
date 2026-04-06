#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary.keys())
    for i in sorted_k:
        print(f"{i}: {a_dictionary[i]}")

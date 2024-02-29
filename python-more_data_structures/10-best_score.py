#!/usr/bin/python3
# This script IS a function that returns the key with the biggest value.
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    key = new_dir.keys()
    for i in key:
        new_dir[i] *= 2
    return(new_dir)
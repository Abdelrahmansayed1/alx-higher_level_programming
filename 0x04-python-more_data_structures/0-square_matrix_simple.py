#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new_list = matrix.copy()
        for i in range(len(new_list)):
            new_list = map( lambda x: x**2,matrix(i))
        return(new_list)
    
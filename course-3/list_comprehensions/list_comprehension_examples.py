#!/usr/bin/env python3

import pprint
import matrix

def use_for_loop():
    numbers_list = [0,1,2,3,4,5,6,7,8,9]
    pprint.pprint(numbers_list)
    even_numbers = []
    for ITEM in numbers_list:
        if not(ITEM % 2):
            even_numbers.append(ITEM)
    pprint.pprint(even_numbers)
    return

def use_list_comprehension():
    '''
    Create a list comprehension
    A list comprehension has 3 parts
    new_list = [OUTPUT_EXPRESSION ITERATION PREDICATE_EXPRESSION]
    '''
    numbers_list = [0,1,2,3,4,5,6,7,8,9]
    pprint.pprint(numbers_list)
    even_numbers = [ITEM for ITEM in numbers_list if not(ITEM % 2)]
    pprint.pprint(even_numbers)
    return

def list_compr_without_predicate():
    numbers_list = [0,1,2,3,4,5,6,7,8,9]
    pprint.pprint(numbers_list)
    all_numbers = ["new " + str(ITEM) for ITEM in numbers_list]
    pprint.pprint(all_numbers)
    all_alt_numbers = ["newer {}".format(ITEM) for ITEM in numbers_list]
    pprint.pprint(all_alt_numbers)
    return

def flatten_2d_matrix_for_loop():
    the_matrix = matrix.create_2d_matrix_auto(n=3,m=3,w=3)
    pprint.pprint(the_matrix)
    flattened = []
    i=0
    for row in the_matrix:
        j=0
        for n in row:
            print('row={};col={} ... n={}'.format(i,j,n))
            flattened.append(n)
            j+=1
        i+=1
    pprint.pprint(flattened)
    return

def flatten_2d_matrix_list_comp():
    the_matrix = matrix.create_2d_matrix_auto(n=3,m=3,w=3)
    flattened = [n for row in the_matrix for n in row]
    pprint.pprint(flattened)
    return

def flatten_3d_matrix_list_comp():
    the_matrix = matrix.create_3d_matrix_auto(n=3,m=3,w=3)
    flattened = [n for row in the_matrix for n in row]
    pprint.pprint(flattened)
    return

if __name__ == '__main__':
    #print('Using for loop')
    #use_for_loop()
    #print('Using list comprehension')
    #use_list_comprehension()
    #print('List comprehension without predicate')
    #list_compr_without_predicate()
    print('Flatten matrix using for loop')
    flatten_2d_matrix_for_loop()
    print('Flatten matrix using for list comprehension')
    flatten_2d_matrix_list_comp()
    flatten_3d_matrix_list_comp()

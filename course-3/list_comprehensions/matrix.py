#!/usr/bin/env python3

import pprint

def create_2d_matrix_manually():
    a = [[0,1,2],[3,4,5],[6,7,8]]
    pprint.pprint(a)
    return a

def create_3d_matrix_manually():
    a = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]],
         [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
         [[18, 19, 20], [21, 22, 23], [24, 25, 26]]]
    pprint.pprint(a)
    return a

def create_2d_matrix_auto(x=3,y=3,w=0):
    a = [w] * y
    for j in range(y):
        a[j] = [w] * x
    pprint.pprint(a)
    return a

def create_3d_matrix_auto(x=3,y=3,z=3,w=0):
    a = [ [ [w for col in range(x)] for col in range(y)] for row in range(z)]
    pprint.pprint(a)
    return a
        
def create_3d_matrix_auto_for_loop(x=3,y=3,z=3,w=0):
    a = [[w]] * z
    for k in range(z):
        for j in range(y):
            a[j] = [w] * x
    pprint.pprint(a)
    return a

if __name__ == '__main__':
    #create_2d_matrix_manually()
    #create_2d_matrix_auto(w=5)
    #create_2d_matrix_auto(x=3,y=4,w=1)
    #create_2d_matrix_auto()
    #create_3d_matrix_manually()
    create_3d_matrix_auto(x=2,y=2,z=2,w=0)
    create_3d_matrix_auto_for_loop(x=2,y=2,z=2,w=1)

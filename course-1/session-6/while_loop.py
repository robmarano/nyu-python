#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a_str = sys.argv[1]
    b_str = sys.argv[2]
    a = int(a_str)
    b = int(b_str)
    while ( a <= b ):
        print("a = " + str(a) + "(b=" + str(b) + ")")
        a = a + 1

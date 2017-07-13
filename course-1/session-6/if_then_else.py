#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if ( a > b ):
        print("a > b")
    elif ( a < b ):
        print("a < b")
    else:
        print("a = b")

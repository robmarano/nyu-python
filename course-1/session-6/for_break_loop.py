#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    a_str = sys.argv[1]
    b_str = sys.argv[2]
    a = int(a_str)
    b = int(b_str)
    inc = 1
    for n in range(a, b+inc):
        for x in range(2, n):
            print(x,n)
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')


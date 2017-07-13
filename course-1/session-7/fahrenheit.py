#!/usr/bin/env python3

import sys

def to_celsius(degF):
    degC = 5/9*(degF - 32)
    return degC

def main():
    degF_str = sys.argv[1]
    try:
        degF = float(sys.argv[1])
        print(to_celsius(degF))
    except ValueError:
        print('Unable to continue since ' + degF_str + ' is not a number.')
        exit(1)
    exit(0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys

def to_celsius(degF):
    degC = 5/9*(degF - 32)
    return degC

def main():
    degF = float(sys.argv[1])
    print(to_celsius(degF))

if __name__ == '__main__':
    main()

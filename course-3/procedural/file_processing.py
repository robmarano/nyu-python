#!/usr/bin/env python3

import re

def main():
    file = open('test.txt', 'r')
    my_dict = {}
    for line in file:
        line = line.strip()
        if line != '':
            k, v = line.split(' ')
            my_dict[k] = v
            print("{} = {}".format(k, v))
            print("{}".format(my_dict))
    file.close()

if __name__ == '__main__':
    main()

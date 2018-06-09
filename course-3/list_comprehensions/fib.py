#!/usr/bin/env python3

from itertools import islice
import pprint

class fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

def fib_gen():
    prev,curr = 0,1
    while True:
        yield curr
        prev,curr = curr, prev+curr

if __name__ == '__main__':
    f = fib_gen()
    fib_list = list(islice(f,0,21))
    pprint.pprint(fib_list)

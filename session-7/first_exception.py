#!/usr/bin/env python

try:
    10/0
except ZeroDivisionError:
    print('Caught division by zero')



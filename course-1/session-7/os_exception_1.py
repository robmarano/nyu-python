#!/usr/bin/env python

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError as err2:
    print("Could not convert data to an integer. {0}".format(err2))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
print("end of program")

#!/usr/bin/env python3

from mylib.shapes import Rectangle as R

# initialize logging for this application
logging.basicConfig(filename='shapes.log',level=logging.DEBUG)

if __name__ == '__main__':
#    shapes.shapes_global = 2
#    print(mylib.shapes.shapes_global)
    my_rectangle = R.Rectangle(20, 10)
    pass

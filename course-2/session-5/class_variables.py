#!/usr/bin/env python3

class Shape(object):
    LIZT = []
    def __init__(self):
        Shape.LIZT.append(self)

    def __str__(self):
        return('SHAPE:from __str__: {}'.format(Shape.LIZT))

    def __repr__(self):
        return('SHAPE: from __repr__: {} {}'.format(self,Shape.LIZT))

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

if __name__ == '__main__':
    a = Circle(5)
    print(a)
    b = Circle(2)
    print(b)
    print(Shape)



#!/usr/bin/env python3

from shapes import Shape

class Square(Shape):
    ''' class Square '''
    def __init__(self, side=1):
        self.side = side
        super().__init__()

    def area(self):
        return self.side ** 2


#!/usr/bin/env python3

from shapes import Shape

class Circle(Shape):
    ''' class Circle '''
    pi = 3.14159
    def __init__(self, radius=1):
        self.radius = radius
        super().__init__()

    def area(self):
        return self.radius ** 2 * Circle.pi


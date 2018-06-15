#!/usr/bin/env python3

import abc

class Shape(abc.ABC):
    ''' Shape class '''
    def __init__(self):
        ''' Shape constructor '''
        super().__init__()
        pass

    @abc.abstractmethod
    def area(self):
        ''' calculate area for Shape subclassed object '''
        pass

class Square(Shape):
    ''' class Square '''
    def __init__(self, side=1):
        self.side = side
        super().__init__()
        pass

    def area(self):
        return self.side ** 2

class Circle(Shape):
    ''' class Circle '''
    pi = 3.14159
    def __init__(self, radius=1):
        self.radius = radius
        super().__init__()
        pass

    def area(self):
        return self.radius ** 2 * Circle.pi


if __name__ == '__main__':
    my_shape = Square(10)
    print(my_shape.area())

    exit(0)

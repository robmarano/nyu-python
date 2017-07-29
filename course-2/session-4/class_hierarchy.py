#!/usr/bin/env python3

class Shape(object):
    def __init__(self, edge_length=1):
        self.edge_length = edge_length
    @property
    def edge(self):
        return self.edge_length
#    def __str__(self):
#        to_string = 'edge_length = {}'.format(self.edge_length)
#        return to_string

class Triangle(Shape):
    ''' Triangle class '''
#    def _init__(self, edge_length):
#    def __init__(self):
#        super().__init__(edge_length)
#        return
#    def __str__(self):
#        to_string_self = 'edge_length = {}'.format(self.edge_length)
        #to_string_super = 'super: edge_length = {}'.format(Shape.edge_length)
        #to_string = '{}\n{}'.format(to_string_super,to_string_self)
#        return to_string_self

class EquilateralTriangle(Triangle):
    ''' Equilateral Triangle '''
    @staticmethod
    def __Calc_area(a):
        return a**2 * 3**0.5 / 4
    def __init__(self,edge_length):
        super().__init__(edge_length)
        self.__area = EquilateralTriangle.__Calc_area(self.edge_length)
        return
    @property
    def area(self):
        return self.__area

class Isosceles(Triangle):
    def __init__(self):
        return


if __name__ == '__main__':
#    s = Shape(10)
#    print(s.edge)
    tt = Triangle(4)
    print(tt)
    print(tt.edge_length)
    t = EquilateralTriangle(5)
    print(t)
    print(t.edge_length)
    print(t.area)

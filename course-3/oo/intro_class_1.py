#!/usr/bin/env python3

class Circle:
    # class variables
    __pi = 3.14159
    def __init__(self,radius=1):
        # instance variables
        self.radius = radius
    # instance methods
    def area(self):
        return self.radius**2 * Circle.__pi

if __name__ == '__main__':
    my_circle = Circle(5)
    print(my_circle)
    for x in dir(Circle):
        print(x)
    print(Circle._Circle__pi)
'''
#    Circle.pi = 0
    print(my_circle.area())
    print(2 * _Circle__pi * my_circle.radius)
    my_circle.radius = 10
    print(my_circle.area())
    print(2 * _Circle__pi * my_circle.radius)
'''

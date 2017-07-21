#!/usr/bin/env python3

class Circle:
    # class variables
    pi = 3.14159
    def __init__(self,radius=1):
        # instance variables
        self.radius = radius
    # instance methods
    def area(self):
        return self.radius**2 * Circle.pi

if __name__ == '__main__':
    my_circle = Circle(5)
    print(Circle.pi)
    print(my_circle.area())
    print(2 * Circle.pi * my_circle.radius)
    my_circle.radius = 10
    print(my_circle.area())
    print(2 * Circle.pi * my_circle.radius)


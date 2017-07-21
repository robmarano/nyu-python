#!/usr/bin/env python3

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y

class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x,y)
        self.__id = 123
        self.side = side

class Circle(Shape):
    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x,y)
        self.__id = 123
        self.radius = radius

if __name__ == '__main__':
    mySquare = Square(10,10,10)
    myCircle = Circle(5,5,5)
    print(mySquare)
    print(myCircle)

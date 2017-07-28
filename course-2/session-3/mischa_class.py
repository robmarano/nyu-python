#!/usr/bin/env python3

class triangle:
    def __init__(self, base = 0):
        self.base = base
        self.shape_type = "triangle"
        self.allies = []
        self.enemies = []
    def area(self):
        return (3**0.5) / 4 * self.base**2 
    def perimeter(self):
        return self.base * 3
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def __str__(self):
        to_string = 'base = {}. shape_type = {}. allies = {}, enemies = {}'.format(self.base, self.shape_type, self.allies, self.enemies)
        return to_string
        
class square:
    def __init__(self, side = 0):
        self.side = side
        self.shape_type = "square"
        self.allies = []
        self.enemies = []

    def area(self):
        return self.side * self.side
    def __str__(self):
        print("Role: complacent and bureacratic")
    def perimeter(self):
        return self.base * 4
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies

class circle:
    pi = 3.14159
    
    def __init__(self, radius = 0):
        self.radius = radius
        self.shape_type = "circle"
        self.allies = []
        self.enemies = []
    def area(self):
        return self.radius**2 * self.__class__.pi
    def perimeter(self):
        return self.radius * 2 * self.__class__.pi
    def update_edge_length(self, change):
        self.base = self.base + change
        return self.base
    def add_ally(self,shape_object):
        self.allies.append(shape_object)
        return self.allies
    def add_enemies(self,shape_object):
        self.enemies.append(shape_object)
        return self.enemies
    def __str__(self):
        print("Role: wise and noble")

if __name__ == "__main__":
    t = triangle(4)
    print(str(t))
    c = circle(1)
    s = square(1)
    t.add_ally("circle")
    t.add_enemies("square")
    c.add_ally("tiangle")
    c.add_enemies("square")
    s.add_enemies("triangle")
    s.add_enemies("square")
    print(t.shape_type)
    print("friends:",t.allies)
    print("enemies:",t.enemies)
    print(c.shape_type)
    print("friends:",c.allies)
    print("enemies:",c.enemies)
    print(s.shape_type)
    print("friends:",s.allies)
    print("enemies:",s.enemies)
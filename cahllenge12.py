import math

class Apple:
    def __init__(self, color, weight, size, cost):
        self.color = color
        self.weight = weight
        self.size = size
        self.cost = cost

class Circle:
    def __init__(self,r):
        self.hankei = r

    def area(self):
        return pow(self.hankei,2) * math.pi
    
circle = Circle(10)
print(circle.area())

class Triangle:
    def __init__(self,t,h):
        self.teihen = t
        self.height = h
    
    def area(self):
        return self.teihen * self.height / 2

triangle = Triangle(10,5)
print(triangle.area())

class Hexagon:
    def __init__(self,l):
        self.len = l
    
    def calculate_perimeter(self):
        return self.len * 6

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter())
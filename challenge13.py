class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,a1,a2,b1,b2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
    
    def calculate_permeter(self):
        return self.a1 + self.a2 + self.b1 + self.b2
    
class Square(Shape):
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    
    def calculate_permeter(self):
        return self.a1*2 + self.a2*2
    
    def change_size(self,w,l):
        self.a1 = self.a1 + w
        self.a2 = self.a2 + l
    



a_rectangle = Rectangle(1,2,3,4)
print(a_rectangle.calculate_permeter())
a_rectangle.what_am_i()

a_square = Square(5,5)
print(a_square.calculate_permeter())
a_square.what_am_i()

class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self,rider):
        self.rider = rider

a_rider = Rider("Yuichi")
a_horse = Horse("Deep Impact", a_rider)


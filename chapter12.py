class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days*temp

or1 = Orange(10,"dark orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)

orange = Orange(200,"orange")
print(orange.mold)
orange.rot(10,37)
print(orange.mold)

class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    
    def change_size(self, w ,l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())
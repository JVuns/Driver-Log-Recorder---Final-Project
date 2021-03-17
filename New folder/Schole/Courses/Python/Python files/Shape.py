class Rectangle:
    
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length**2

class Triangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length
    def area(self):
        return self.length*self.height/2

rect = Rectangle(5)
tri = Triangle(3,6)
print(rect.area())
print(tri.area())

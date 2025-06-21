import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = int(radius)
        return math.pi * self.radius ** 2
    

        
        
import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        area = self.length * self.width
        return area
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        area = math.pi * self.radius ** 2
        return area
    

        
        
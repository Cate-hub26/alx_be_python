import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
        area = self.length * self.width
        return area
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = int(radius)
        area = math.pi * self.radius ** 2
        return area
    

        
        
import math

class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = int(radius)
        area_of_circle = math.pi * self.radius ** 2
        return area_of_circle
    

        
        
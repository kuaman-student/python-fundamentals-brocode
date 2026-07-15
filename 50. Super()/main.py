# super() : Function used in a child class to call methods from a parent class (superclass). 
# Allows you to extend the functionality of the inherited methods



class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class Rectangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width 
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Color: {self.color}\nFilled:{self.is_filled}\nArea:{self.area()}"





class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side 

    def area(self):
        return self.side * self.side

    def __str__(self):
        return f"Color: {self.color}\nFilled:{self.is_filled}\nArea:{self.area()}"

from math import pi
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius 

    def area(self):
        return self.radius * pi

    def __str__(self):
        return f"Color: {self.color}\nFilled:{self.is_filled}\nArea:{self.area()}"




rectangle = Rectangle("Red", True, 5, 3)
square = Square("Blue", False, 5)
circle = Circle("White", False, 10.2)

print(rectangle)
print(square)
print(circle)
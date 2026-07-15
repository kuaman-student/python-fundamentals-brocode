# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.


# Polymorphis : Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe = Form
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance =  An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

import math
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * math.pi


class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(5), Rectangle(2,3), Square(3), Pizza(5, True)]

for shape in shapes:
    print(f"Area: {shape.area()}")
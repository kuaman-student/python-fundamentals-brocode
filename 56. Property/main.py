# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: Add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, height, width):
        self._width =width #made private
        self._height = height #made private

    @property
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be positive.")
    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("Height must be positive.")

    @width.deleter
    def width(self):
        print("Width has been deleted")
    @height.deleter
    def height(self):
        print("Height has been deleted")
rectangle = Rectangle(2.322, 3)
print(rectangle._width)
print(rectangle._height)
rectangle.width = 0
rectangle.width = 5
rectangle.height = 2
del rectangle.width
del rectangle.height

print(rectangle._width)
print(rectangle._height)
        
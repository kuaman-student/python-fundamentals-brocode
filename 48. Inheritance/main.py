# Inheritance Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def walk(self):
        print(f"{self.name} is walking")



class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
class Mouse(Animal):
    def speak(self):
        print("squeak")


dog1 = Dog("tom")
cat1 = Cat("Catty")
mouse1 = Mouse("Micy")
print(dog1.name)
print(cat1.name)
print(mouse1.name)
dog1.walk()
cat1.walk()
mouse1.walk()
dog1.speak()
cat1.speak()
mouse1.speak()
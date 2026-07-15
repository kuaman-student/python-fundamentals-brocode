# OOP stands for Object-Oriented Programming.

# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code


# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object is created based on that class. For example:



# object: a bundle of related attributes {variables} and methods {functions} 
# class: (blueprint) used to design the sructure and layout of the object
# you need a class to create many objects


# Class	Objects
# Fruit	Apple, Banana, Mango
# Car	Volvo, Audi, Toyota





# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

p1 = MyClass()
print(p1)
print(p1.x)

# Delete the p1 object:

del p1
# print(p1.x)


p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)















# __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

class Car:
  def __init__(self, model, color, year):
    self.model = model
    self.color = color
    self.year = year


car1 = Car("model1", "red", 2020)
print(car1.model)
print(car1.color)
print(car1.year)
car2 = Car("model2", "year", 2021)
print(car2.model)
print(car2.color)
print(car2.year)

# Without the __init__() method, you would need to set properties manually for each object:
car1.for_sale = True
print(car1.for_sale)
# print(car2.for_sale)




# Set a default value for the age parameter:

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)



import person

person1 = person.Person("AK", 18, False, "India")
print(person1.greet())
print(person1.welcome())
print(person1.ishuman)
person2 = person.Person("AK2", 20, True)
print(person2.greet())
print(person2.welcome())
print(person2.ishuman)


# When you modify a class property, it affects all objects:

person.Person.ishuman = False

print(person1.ishuman)
print(person2.ishuman)

print(person1)
print(person2)
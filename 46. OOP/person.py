class Person:

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
    ishuman = True

# Properties defined inside __init__() belong to each object (instance properties).
    def __init__(self, name, age, is_employed, country="India"):
# Without self, Python would not know which object's properties you want to access:
        self.name = name
        self.age = age
        self.country = country
        self.is_employed = is_employed
    
    def greet(self): #this is a method: (actions that an object can perform)
        return "Hello " + self.name
    def welcome(self):
        return self.greet() + f". U are from {self.country}."


    # The __str__() method is a special method that controls what is returned when the object is printed:
    def __str__(self):
        if self.is_employed:
            employment = "employed"
        else:
            employment = "not employed"
        return f"Hello, this is {self.name}, aged {self.age}years, from {self.country} and is {employment}"       
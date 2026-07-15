#multiple inheritance inherit from more than one parent class
# C(A, B)
#multilevel inheritance inherit from a parent which inherits from another parent
# C(B) <- B(A) <- A


class Animal:
    def __init__(self, name):
            self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def walk(self):
        print(f"{self.name} is walking")
    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

#     When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#    Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

    def __init__(self, name, biosphere):
        # Animal.__init__(name)
        super().__init__(name)
        self.biosphere = biosphere
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Rabbi", "Ground")
hawk = Hawk("hawky")
fish = Fish("Fishy", "Water")



rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()


rabbit.biosphere
fish.biosphere

rabbit.sleep()
rabbit.walk()
hawk.sleep()
hawk.walk()
fish.sleep()
fish.walk()
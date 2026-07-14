# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.


# Create a Module
# To create a module just save the code you want in a file with the file extension .py:


def greeting(name):
  print("Hello, " + name)


import math
# print(help(math))
import math as m
print(m.pi)

from math import pi
print(pi)

from math import e
print(e)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
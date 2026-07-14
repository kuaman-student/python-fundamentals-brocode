# syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

# Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [x*3 for x in range(1,11)]
print(triples)

triples = [int(x*3/2) for x in doubles]
print(triples)



numbers = [1,2,3 -2, -5, 10, 8, -10]
print(numbers)
positive = [number for number in numbers if number>=0]

print(positive)

grades = [20, 30 , 40 , 15, 70, 80 , 90, 99, 33, 32, 35]


passing_grades = [grade for grade in grades if grade>33]
print(passing_grades)
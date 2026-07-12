# List: ordered collection of items. It is mutable, meaning you can add, remove, or modify items after creation.

# Tuple: ordered collection of items. It is immutable, meaning its elements cannot be altered once defined.

# Set: unordered, unique items. It is mutable for adding or removing items, but it prevents duplicate values.

fruits = ('apple', 'mango', 'banana', 'grapes', 'guava', 'guava')
# print(help(fruits))
# print(dir(fruits))

print(fruits)
print(len(fruits))


# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
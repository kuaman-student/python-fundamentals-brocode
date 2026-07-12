# List: ordered collection of items. It is mutable, meaning you can add, remove, or modify items after creation.

# Tuple: ordered collection of items. It is immutable, meaning its elements cannot be altered once defined.

# Set: unordered, unique items. It is mutable for adding or removing items, but it prevents duplicate values.

fruits = ['apple', 'mango', 'banana', 'grapes', 'guava']
# print(help(fruits))
# print(dir(fruits))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
fruits.append("Papaya")
print(fruits)
print(len(fruits))


newfruits = fruits.copy()
print(newfruits)

print(fruits.count("mango"))

fruits.extend(newfruits)
print(fruits)

print(fruits.index("mango"))

fruits.insert(1, "Great Mango")
print(fruits)

print(fruits.pop(1))
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print("apple" in fruits)
for fruit in fruits:
    print(fruit, end='-')

print()
fruits.clear()
print(fruits)
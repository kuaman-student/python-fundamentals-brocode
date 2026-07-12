# List: ordered collection of items. It is mutable, meaning you can add, remove, or modify items after creation.

# Tuple: ordered collection of items. It is immutable, meaning its elements cannot be altered once defined.

# Set: unordered, unique items. It is mutable for adding or removing items, but it prevents duplicate values.

fruits = {'apple', 'mango', 'banana', 'grapes', 'guava'}
# print(help(fruits))
# print(dir(fruits))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

fruits.add("pineapple")
print(fruits)

fruits2 = {'apple', 'mango', 'banana', "pizza", "burger"}
print(fruits.difference(fruits2))

print(fruits)
fruits.difference_update(fruits2)
print(fruits)

fruits.discard("apple")
fruits.discard("pineapple")
print(fruits)

fruits.update(fruits2)
print(fruits)


fruits.clear()
print(fruits)
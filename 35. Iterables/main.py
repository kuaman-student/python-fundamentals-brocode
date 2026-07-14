# an iterable is any object capable of returning its elements one at a time, allowing it to be looped over using a loop.


# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

for tup in mytuple:
    print(tup)

mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

for str in mystr:
    print(str)


mydict = {"A":1, "B":2, "C":3}
for key, value in mydict.items():
    print(f"{key}:{value}")
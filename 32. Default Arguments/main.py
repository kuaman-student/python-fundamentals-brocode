# parameters with predefined values. This means you don’t always need to pass every argument while calling a function.

# If you provide a value, Python uses it.
# If you skip it, the default value is used automatically.

def greet(name="Guest"):
    print("Hello,", name)

greet()          
greet("Kate")

# def hello(name = "guest", age): => wrong
def hello(age, name = "guest"):
    print(f"Hello {name}, aged {age}")

hello(21)
hello(18, "ak")

# This example shows the problem of using a list as a default argument. The same list is reused across calls.

def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item('note'))
print(add_item('pen'))
print(add_item('eraser'))

# Explanation: The same list lst is reused, so items keep accumulating.

# Example 5: This example shows the same problem when using a dictionary as a default argument.
def add_dict(item, qty, d={}):
    d[item] = qty
    return d

print(add_dict('note', 4))
print(add_dict('pen', 1))
print(add_dict('eraser', 1))

# Explanation: The same dictionary d is reused, so all items are stored together.


# Example 6: This example shows the correct way use None as the default and create a new list or dictionary inside the function.

def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(add_item('note'))
print(add_item('pen'))
print(add_item('eraser'))


def add_dict(item, qty, d=None):
    if d is None:
        d = {}
    d[item] = qty
    return d


print(add_dict('note', 4))
print(add_dict('pen', 1))
print(add_dict('eraser', 1))

# Explanation: Each time the function is called without arguments, a new list or dictionary is created. This prevents sharing between calls.




#  the order of arguments in Python does matter.
# 1)Positional arguments (must come first)
# 2)Default (Keyword) arguments
# 3) Arbitrary positional (*args)
# 4)Keyword-only arguments
# 5)Arbitrary keyword (**kwargs)
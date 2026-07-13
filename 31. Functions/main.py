# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def hello():
    print("Hello")
def hello_name(name):
    print(f"Hello {name}")


name = input("Enter your name:\t")
def add(a,b):
    return a+b
hello()
hello_name(name)

print(add(2,3))
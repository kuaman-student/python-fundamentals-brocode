# #Decorator
# A function that extends the behavior of another function
# w/o modifying the base function
# Pass the base function as an argument to the decorator
# @add_sprinkles
# get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Sprinkles added ♨️")
        func(*args, **kwargs) #if this not added, the get_ice_cream fn will not run
    return wrapper

def extra_cream(func):
    def wrapper(*args, **kwargs):
            print("Extra Cream added 🍨")
            func(*args, **kwargs)
    return wrapper
@extra_cream
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your ice cream of {flavour} flavour.🍧")

get_ice_cream("Vanilla")
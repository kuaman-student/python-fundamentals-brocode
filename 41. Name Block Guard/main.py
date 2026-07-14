def my_function():
    print("This function is ready to be used!")

# The Idiom/Guard Block

print(__name__)
# "Dunder" most commonly refers to "double underscore"
if __name__ == "__main__":
    # This code only runs if you execute this file directly
    print("Script executed directly. main.py")
    my_function()


# if __name__ == "__main__" (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
# helps readability,
# Leaves no global variables
# avaid unintended execution
# Ex. Asbrary Sport library for functionality When running library directly, display a help page
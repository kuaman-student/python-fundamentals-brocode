import math
print("Calculating circumference of a circle.\n")
radius = float(input("Enter radius of circle:\t"))
circumference = round(2*math.pi*radius, 3)
print(f"\nCircumference of Circle is {circumference} units.")
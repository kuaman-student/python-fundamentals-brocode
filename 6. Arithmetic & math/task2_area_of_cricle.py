import math
print("Calculating area of a circle.\n")
radius = float(input("Enter radius of circle:\t"))
area = round(math.pi*math.pow(radius, 2), 3)
print(f"\nArea of Circle is {area} sq units.")
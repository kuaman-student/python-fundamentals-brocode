import math
print("Calculating Hypotenuse of a Right Triangle.\n")
base = float(input("Enter length of base:\t"))
perp = float(input("Enter length of perpendicular:\t"))
hyp = round(math.pow(math.pow(base, 2) + math.pow(perp, 2), 0.5), 2)
print(f"\nHypotenuse of the Right Triangle is {hyp}units.")
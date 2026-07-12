foods = []
prices = []
quantities = []
total = 0
food = ""
while food!= "q":
    print("\n\n\n")
    food = input("Name the food u want ('q' for end):\t")
    if food == "q":
        break
    foods.append(food)
    qty = float(input(f"Enter the quantity of {food} u want:\t"))
    quantities.append(qty)
    price = float(input(f"Enter the Price of {food}:\t"))
    prices.append(price)

print("\n\n\n")
for counter in range(0, len(foods)):
    price = (prices[counter] * quantities[counter])
    print(f"{foods[counter]} X {quantities[counter]}:\t {prices[counter]}*{quantities[counter]}:\t{price}")
    total+= price

print(f"Total Bill: {total} for {len(foods)} items.")
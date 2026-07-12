menu = {
    "spring rolls": 6.50,
    "garlic bread": 5.00,
    "tomato soup": 5.50,
    "grilled salmon": 18.50,
    "chicken alfredo": 14.99,
    "vegetable stir fry": 12.00,
    "chocolate lava cake": 7.00,
    "fresh orange juice": 4.50,
    "mineral water": 2.50,
}

print("-------------------Menu-------------------")
for key in menu:
    print(f"{key:30} : {menu[key]:.2f}")
print("------------------------------------------")

foods = []
total = 0

while True:
    food = input("\nEnter the food u want (q for quit):\t").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        foods.append(food)
        print(f"Added {food} to the list")
        total += menu[food]
    else:
        print(f"{food} is not in the list")


print("\nYou ordered:\n")
for food in foods:
    print(food, end="\n")

print(f"\nTotal: {total}")

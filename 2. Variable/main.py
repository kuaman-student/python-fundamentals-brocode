first_name = "Aman"
last_name = "Kumar"
food = "Pizza"
email = "abcd.gmail.com"
age = 18
food_qty = 5
price = 99.99
isStudent = True

print(f"Hello {first_name} {last_name}.")
print(f"Your email is {email}.")
print(f"Your age is {age}.")
print(f"Your like {food}.")
print(f"You are buying {food_qty} {food}.")
print(f"Price is {price} per {food}.")
print(f"Total Price is ",  price*food_qty)
if isStudent:
    print("You are a student.")
else:
    print("You are not a student.")
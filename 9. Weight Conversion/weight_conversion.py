weight = float(input("Enter your weight:\t"))
unit = input("You entered weight in kg or pound(K or L):\t")
if(unit == "K" or unit == "k"):
    print(f'Weight in kg: {weight}\nWeight in Pounds: {round(weight*2.20462, 2)}')
elif(unit == "L" or unit == "l"):
    print(f'Weight in kg: {round(weight*0.453592, 2)}\nWeight in Pounds: {weight}')
else:
    print("Invalid Inputs")

temp = float(input("Enter the Temperature:\t"))
unit = input("You entered weight in Celsius, Fahrenheit or Kelvin scale(C, F or K):\t")

if(unit == "c" or unit == "C"):
    print(f"Temperature in Celsius(°C): {round(temp, 2)}°C")
    print(f"Temperature in Fahrenheit(°F): {round((temp*1.8)+32, 2)}°F")
    print(f"Temperature in Kelvin(K): {round(temp+273.15, 2)}K")
elif(unit == "f" or unit == "F"):
    print(f"Temperature in Celsius(°C): {round((temp-32)*1.8, 2)}°C")
    print(f"Temperature in Fahrenheit(°F): round({temp}, 2)°F")
    print(f"Temperature in Kelvin(K): {round(((temp-32)*1.8)+273.15, 2)}K")
elif(unit == "k" or unit == "K"):
    print(f"Temperature in Celsius(°C): {round(temp - 273.15, 2)}°C")
    print(f"Temperature in Fahrenheit(°F): {round(((temp-273.15)*1.8)+32, 2)}°F")
    print(f"Temperature in Kelvin(K): {round(temp, 2)}K")
else:
    print('Please enter valid inputs.')
num1 = float(input("Enter the 1st number:\t"))
num2 = float(input("Enter the 2nd number:\t"))
operator = input("Enter the operation u want (+, -, *, /, **):\t")
if(operator == "+"):
    print(round(num1 + num2), 2)
elif(operator == "-"):
    print(round(num1 - num2), 2)
elif(operator == "*"):
    print(round(num1 * num2), 2)
elif(operator == "/"):
    print(round(num1 / num2), 2)
elif(operator == "**"):
    print(round(num1**num2, 2))
else:
    print("Enter valid operator")
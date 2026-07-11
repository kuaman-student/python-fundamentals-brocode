print("Lets create a rectangular pattern")
rows = int(input("Enter Number of rows:\t"))
columns = int(input("Enter Number of columns:\t"))
symbol = input("Enter a symbol u want:\t")

for rows in range(0, rows):
    for cols in range(0, columns):
        print(symbol, end=" ")
    print()
p = input("Enter Principal amount:\t")
while not(p.isnumeric or p<=0 ):
    p = input("Enter correct Principal amount:\t")

r = input("Enter Interest rate(in decimals):\t")
while not(r.isnumeric or r<0 ):
    r = input("Enter correct Interest rate(in decimals):\t")

n = input("Enter Number of times that interest is compounded per year:\t")
while not(n.isnumeric or n<=0 ):
    n = input("Enter correct Number of times that interest is compounded per year:\t")

t = input("Enter time period in years:\t")
while not(p.isnumeric or p<=0 ):
    t = input("Enter correct time period in years:\t")

p = int(p)
r = int(r)
n = int(n)
t = int(t)

amount = p*((1+(r/n))**(n*t))
print(f'Principal: {p}\nInterest rate(in decimals): {r}%\nNumber of times that interest is compounded per year: {n}\nTime: {t}\nFinal Amount u will get: {amount}')
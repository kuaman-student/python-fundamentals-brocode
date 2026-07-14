#python banking program

# show balance
# deposit
# withdraw


import home

print(f'''
    *****************************
           Banking Program
    *****************************
    Let's first create your account
    ''')

name = input("Please enter your name:\t")
pin = input("Please choose a 4-digit pin:\t")
while True:
    if pin.isnumeric():
        pin = int(pin)
        if pin >= 1000 and pin <=9999:
            break
        else:
            pin = input("Please choose a correct 4-digit pin:\t")
    else:
        pin = input("Please choose a correct 4-digit pin:\t")


pin = int(pin)
home.home_page(name, pin)
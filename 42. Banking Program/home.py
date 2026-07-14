def validate(name, pin):
    while True:
        user_pin = input(f"\nWelcome {name}\nPlease confirm your PIN: ")

        if user_pin.isdigit():
            user_pin = int(user_pin)
            break
        else:
            print("PIN should contain only digits.")

    return user_pin == pin


def show_balance(name, pin, balance):
    if validate(name, pin):
        print("\n*****************************")
        print("      ACCOUNT DETAILS")
        print("*****************************")
        print(f"Account Holder : {name}")
        print(f"Current Balance: ₹{balance}")
        print("*****************************")
    else:
        print("Wrong PIN!")


def deposit(name, pin, balance, history):
    if not validate(name, pin):
        print("Wrong PIN!")
        return balance

    while True:
        amount = input("Enter amount to deposit: ")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break

        print("Enter a valid amount.")

    balance += amount
    history.append(amount)

    print("\n******** RECEIPT ********")
    print(f"Deposited : ₹{amount}")
    print(f"Balance   : ₹{balance}")
    print("*************************")

    return balance


def withdraw(name, pin, balance, history):
    if not validate(name, pin):
        print("Wrong PIN!")
        return balance

    if balance == 0:
        print("No money in your account.")
        return balance

    while True:
        amount = input("Enter amount to withdraw: ")

        if amount.isdigit():
            amount = int(amount)

            if amount <= 0:
                print("Amount must be greater than zero.")

            elif amount > balance:
                print(f"Insufficient Balance! Available ₹{balance}")

            else:
                break

        else:
            print("Enter a valid amount.")

    balance -= amount
    history.append(-amount)

    print("\n******** RECEIPT ********")
    print(f"Withdrawn : ₹{amount}")
    print(f"Balance   : ₹{balance}")
    print("*************************")

    return balance


def transaction_history(name, pin, history):
    if not validate(name, pin):
        print("Wrong PIN!")
        return

    print("\n*****************************")
    print("    TRANSACTION HISTORY")
    print("*****************************")

    if len(history) == 0:
        print("No Transactions Yet.")
        return

    for transaction in history:
        if transaction > 0:
            print(f"Deposited : ₹{transaction}")
        else:
            print(f"Withdrawn : ₹{-transaction}")


def last_transactions(name, pin, history):
    if not validate(name, pin):
        print("Wrong PIN!")
        return

    if len(history) == 0:
        print("No Transactions Yet.")
        return

    while True:
        n = input("How many recent transactions do you want to see? ")

        if n.isdigit():
            n = int(n)

            if n > 0:
                break

        print("Enter a valid number.")

    print("\nRecent Transactions\n")

    recent = history[-n:]

    for transaction in reversed(recent):
        if transaction > 0:
            print(f"Deposited : ₹{transaction}")
        else:
            print(f"Withdrawn : ₹{-transaction}")


def home_page(name, pin):
    balance = 0
    history = []

    while True:

        print(f"""
*****************************
      Banking Program
*****************************
1. Show Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Last Transactions
6. Exit
*****************************
Welcome {name}
""")

        choice = input("Enter your choice (1-6): ")

        match choice:

            case "1":
                show_balance(name, pin, balance)

            case "2":
                balance = deposit(name, pin, balance, history)

            case "3":
                balance = withdraw(name, pin, balance, history)

            case "4":
                transaction_history(name, pin, history)

            case "5":
                last_transactions(name, pin, history)

            case "6":
                print("\n*****************************")
                print("Thank You For Banking With Us")
                print("*****************************")
                print(f"Final Balance      : ₹{balance}")
                print(f"Total Transactions : {len(history)}")
                break

            case _:
                print("Invalid Choice.")


# ---------------- MAIN ---------------- #

print("""
*****************************
      Banking Program
*****************************
Let's create your account.
""")

name = input("Enter your name: ")

while True:
    pin = input("Choose a 4-digit PIN: ")

    if pin.isdigit() and len(pin) == 4:
        pin = int(pin)
        break

    print("PIN must be exactly 4 digits.")

home_page(name, pin)
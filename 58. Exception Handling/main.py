# exception
# An event that interrupts the flow of a program (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

try:
    number = int(input("Enter your number:\t"))
    print(1/number)
except ZeroDivisionError:
    print("1/0 not allowed")
except ValueError:
    print("Only Numbers pls")
except Exception:
    print("Something went wrong")
finally:
    print("Clean up")
import random

num = random.randint(1,100)

guess = int(input("Guess a number between 1-100:\t"))
if(guess<=100 and guess>=0):
    counter = 1
else:
    counter = 0

while guess != num:
    if(guess-num>15 and guess<=100 and guess>=0):
        print("\n\nGo down. Your Guess is too high.")
        counter+=1
    elif(guess>num and guess<=100 and guess>=0):
        print("\n\nGo down. Your Guess is high.")
        counter+=1
    elif(num-guess>15 and guess<=100 and guess>=0):
        print("\n\nGo up. Your Guess is too low.")
        counter+=1
    elif(num>guess and guess<=100 and guess>=0):
        print("\n\nGo up. Your Guess is low.")
        counter+=1
    else:
        print("Please enter correct number and in range.")
    print(f"You have used {counter} tries")
    guess = int(input("Guess a number between 1-100:\t"))


print(f"\n\nYeah u guessed correct number: {num}\nYou took {counter} tries.")



import random

choices = ["Rock", "Paper", "Scissor"]

print("Welcome to rock paper scissor game.")

wins = 0
draw = 0
lose = 0

while True:
    response = input("Enter your choice rock, paper or scissor (r, p, s) and (q) for quit:\t").lower()
    if(response == "q"):
        break
    choice = random.randint(0,2)
    if response == "r":
        if choice == 0:
            print(f"User: Rock\nComputer: {choices[choice]}")
            print("\nOhh! Its a draw\n")
            draw+=1
        elif choice ==1:
            print(f"User: Rock\nComputer: {choices[choice]}")
            print("\nI win, U lose.\n")
            lose += 1
        else:
            print(f"User: Rock\nComputer: {choices[choice]}")
            print("\nYeah! You win\n")
            wins+=1
    elif response == "p":
            if choice == 1:
                print(f"User: Paper\nComputer: {choices[choice]}")
                print("\nOhh! Its a draw\n")
                draw+=1
            elif choice ==2:
                print(f"User: Paper\nComputer: {choices[choice]}")
                print("\nI win, U lose.\n")
                lose += 1
            else:
                print(f"User: Paper\nComputer: {choices[choice]}")
                print("\nYeah! You win\n")
                wins+=1
    elif response == "s":
            if choice == 2:
                print(f"User: Scissor\nComputer: {choices[choice]}")
                print("\nOhh! Its a draw\n")
                draw+=1
            elif choice ==0:
                print(f"User: Scissor\nComputer: {choices[choice]}")
                print("\nI win, U lose.\n")
                lose += 1
            else:
                print(f"User: Scissor\nComputer: {choices[choice]}")
                print("\nYeah! You win\n")
                wins+=1
    else:
        print("\nWrong input\n")

print(f"\nYeah! Game End\nTotal rounds: {lose+wins+draw}\nWins: {wins}\nLose: {lose}\nDraw: {draw}")
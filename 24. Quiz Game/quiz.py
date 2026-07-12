# 1. List of 10 simple questions
questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the largest ocean on Earth?",
    "How many days are in a leap year?",
    "Which animal is known as the Ship of the Desert?",
    "What is the color of an emerald?",
    "How many continents are there on Earth?",
    "What is the primary gas found in the air we breathe?",
    "Which fruit is traditionally given to teachers?",
    "What is the boiling point of water in Celsius?"
]

# 2. 2D list containing 4 options for each question
options = [
    ["London", "Berlin", "Paris", "Madrid"],
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    ["365", "366", "364", "367"],
    ["Camel", "Horse", "Elephant", "Donkey"],
    ["Red", "Blue", "Green", "Yellow"],
    ["5", "6", "7", "8"],
    ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
    ["Banana", "Apple", "Orange", "Grape"],
    ["50°C", "90°C", "100°C", "120°C"]
]

# 3. List of correct answers matching the questions
answers = [
    "Paris",
    "Mars",
    "Pacific Ocean",
    "366",
    "Camel",
    "Green",
    "7",
    "Nitrogen",
    "Apple",
    "100°C"
]

options_name = ["a", "b", "c", "d"]
guesses =[]
for x in range(0, len(answers)):
    guesses.append(0)
print(guesses)

print("Welcome to Quiz game, lets start. Enter {a,b,c,d} for selecting options (+4 for every correct answer, -1 for every wrong attempt).\n\n\n")
for x in range(1,len(answers)+1):
    answer = ""
    guess = 0
    while answer != answers[x-1]:
        if(guess != 0):
            print(f"You have taken {guess} attempts.\n")
        print(f"Q{x}: {questions[x-1]}\n")
        for i in range(0,4):
            print(f"{options_name[i]}) {options[x-1][i]}", end="\t")
        guess+=1
        answer = input("\nEnter a,b,c,d:\t")
        answer = options[x-1][options_name.index(answer)]
        guesses[x-1] = guess


print("\n---------------\n|Your analysis|\n---------------")
marks = 0
for x in range(1,len(answers)+1):
    print(f"Q{x})\t{guesses[x-1]} attempts\n")
    marks += ((guesses[x-1] - 1)*-1) + 4
print(f"\nYour Marks: {marks}")
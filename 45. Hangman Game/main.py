import random
phases = {
    1: (
"************",
"  |",
"",
"",
"",
"",
"************")
,
    2: (
"************",
"  |",
"  ○",
"",
"",
"",
"",
"************"),
    3: (
"************",
"  |",
"  ○",
"  |",
"",
"",
"************"),
    4: (
"************",
"  |",
"  ○"
"/ |",
"",
"",
"************")
,
    5: (
"************",
"  |",
"  ○",
"/ | \\",
"",
"",
"************"),
    6: (
"************",
"  |",
"  ○",
"/ | \\",
"  |",
"",
"************"),
    7:
("************",
"  |",
"  ○",
"/ | \\",
"  |",
" / \\",
"************"
),
}

def end(result, attempt, mistakes):
    print(f'''
************
 Game Over
  You {result}
  Attempts: {attempt}
  Wrong: {mistakes}
************
''')
    
def printhangman(mistakes):
    for lines in phases[mistakes]:
        print(lines, end="\n")


words = [
    "python",
    "computer",
    "keyboard",
    "monitor",
    "internet",
    "developer",
    "programming",
    "algorithm",
    "database",
    "compiler",
    "variable",
    "function",
    "debugging",
    "network",
    "machine",
    "galaxy",
    "volcano",
    "elephant",
    "dolphin",
    "umbrella",
    "adventure",
    "treasure",
    "castle",
    "penguin",
    "bicycle"
]

hints = [
    "A popular programming language.",
    "An electronic device used for computing.",
    "Used to type on a computer.",
    "Displays the output of a computer.",
    "A worldwide network connecting devices.",
    "A person who writes software.",
    "The process of writing computer code.",
    "A step-by-step method to solve a problem.",
    "A collection of organized data.",
    "Converts source code into machine code.",
    "Stores a value in programming.",
    "A reusable block of code.",
    "Finding and fixing errors in code.",
    "A group of connected computers.",
    "Learning often follows this word.",
    "A massive collection of stars.",
    "A mountain that erupts with lava.",
    "The largest land animal.",
    "An intelligent sea mammal.",
    "Used to protect yourself from rain.",
    "An exciting and unusual experience.",
    "Hidden wealth waiting to be discovered.",
    "A large fortified building for kings and queens.",
    "A black and white bird that cannot fly.",
    "A two-wheeled vehicle powered by pedaling."
]


def play(word, hint, guessed_chars=[]):
    mistakes = 0
    attempt = 0
    print("Let's begin")
    while True:
        print("\n\n")
        if mistakes == 8:
            end("Lost", attempt, mistakes)
            break
        if len(guessed_chars) == len(word):
            end("Won", attempt, mistakes)
            break
        if mistakes != 0:
            for line in phases[mistakes]:
                print(line)
        for char in word:
            print(f"{char}", end=" ") if char in guessed_chars else print(f"_", end=" ")
        print("\n" + hint)

        guess = input("\nEnter your guess:\t")
        attempt+=1
        if guess not in word:
            mistakes+=1
            print("wrong")
        else:
            print("right")
            guessed_chars.append(guess)




word = random.choice(words)
hint = hints[words.index(word)]
# guessed_char = ["a", "b", "c", "u"]
play(word, hint)

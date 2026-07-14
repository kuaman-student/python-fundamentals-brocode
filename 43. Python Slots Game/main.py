import random
import time

# ================= PAYOUTS ================= #

payout = {
    "🍒": {"triple": 3, "double": 1.2},
    "🍋": {"triple": 4, "double": 1.3},
    "🍇": {"triple": 5, "double": 1.5},
    "🍀": {"triple": 7, "double": 2},
    "🔔": {"triple": 10, "double": 3},
    "⭐": {"triple": 15, "double": 5},
    "❤️": {"triple": 20, "double": 7},
    "💎": {"triple": 30, "double": 10},
    "👑": {"triple": 50, "double": 20},
    "7️⃣": {"triple": 100, "double": 25},
}

# weighted symbols
symbols = [
    "🍒","🍒","🍒","🍒",
    "🍋","🍋","🍋",
    "🍇","🍇",
    "🍀","🍀",
    "🔔",
    "⭐",
    "❤️",
    "💎",
    "👑",
    "7️⃣"
]

# ================= GAME DATA ================= #

balance = 100

games_played = 0
wins = 0
losses = 0

streak = 0
best_streak = 0

highest_balance = balance
biggest_win = 0

history = []

# ================= UI ================= #

print("""
╔══════════════════════════════════════════════════════╗
║              🎰 WELCOME TO PYTHON SLOTS 🎰          ║
╠══════════════════════════════════════════════════════╣
║ Match symbols and multiply your winnings!           ║
║                                                     ║
║ 🎯 3 Matching Symbols → BIG WIN                     ║
║ 🎯 2 Matching Symbols → SMALL WIN                   ║
║ 💎 Rare Symbols = Higher Rewards                    ║
║ 👑 & 7️⃣ are the Ultimate Jackpot Symbols!          ║
║                                                     ║
║ 💰 Starting Balance : ₹100                          ║
╚══════════════════════════════════════════════════════╝
""")

print("""
╔══════════════════════════════════════════════════════╗
║                 💰 PAYOUT TABLE 💰                  ║
╠════════╦══════════════╦══════════════════════════════╣
║ Symbol ║ 3 Match      ║ 2 Match                      ║
╠════════╬══════════════╬══════════════════════════════╣
║ 🍒     ║ x3           ║ x1.2                         ║
║ 🍋     ║ x4           ║ x1.3                         ║
║ 🍇     ║ x5           ║ x1.5                         ║
║ 🍀     ║ x7           ║ x2                           ║
║ 🔔     ║ x10          ║ x3                           ║
║ ⭐     ║ x15          ║ x5                           ║
║ ❤️     ║ x20          ║ x7                           ║
║ 💎     ║ x30          ║ x10                          ║
║ 👑     ║ x50          ║ x20                          ║
║ 7️⃣     ║ x100         ║ x25                          ║
╚════════╩══════════════╩══════════════════════════════╝
""")

# ================= FUNCTIONS ================= #

def show_stats():
    print(f"""
╔══════════════════════════════════════╗
║          📊 GAME STATISTICS          ║
╠══════════════════════════════════════╣
║ 🎮 Games Played : {games_played}
║ 🏆 Wins         : {wins}
║ ❌ Losses       : {losses}
║ 🔥 Streak       : {streak}
║ 🚀 Best Streak  : {best_streak}
║ 💰 Balance      : ₹{balance}
║ 📈 Highest Bal. : ₹{highest_balance}
║ 💎 Biggest Win  : ₹{biggest_win}
╚══════════════════════════════════════╝
""")

    if history:
        print("\nLast 5 Spins:")
        for item in history[-5:]:
            print(item)

def spin():
    global balance
    global games_played
    global wins
    global losses
    global streak
    global best_streak
    global highest_balance
    global biggest_win

    while True:

        bet = input(f"\nEnter Bet Amount (Balance ₹{balance}): ₹")

        if not bet.isdigit():
            print("Enter numbers only.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        if bet > balance:
            print("Insufficient balance.")
            continue

        break

    balance -= bet

    print("\n🎰 Spinning", end="")

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print("\n")

    s1 = random.choice(symbols)
    s2 = random.choice(symbols)
    s3 = random.choice(symbols)

    print("╔══════════════════════╗")
    print("║      🎰 RESULT       ║")
    print("╚══════════════════════╝")

    print(f"\n      {s1} | {s2} | {s3}\n")

    games_played += 1

    result_text = f"{s1} {s2} {s3}"

    # Triple Match

    if s1 == s2 == s3:

        multiplier = payout[s1]["triple"]

        win_amount = int(bet * multiplier)

        balance += win_amount

        wins += 1
        streak += 1

        biggest_win = max(biggest_win, win_amount)

        print("🎉 JACKPOT / TRIPLE MATCH!")
        print(f"Multiplier : x{multiplier}")
        print(f"You Won ₹{win_amount}")

        result_text += f" | WIN ₹{win_amount}"

    # Double Match

    elif s1 == s2 or s2 == s3 or s1 == s3:

        if s1 == s2:
            matched = s1
        elif s2 == s3:
            matched = s2
        else:
            matched = s1

        multiplier = payout[matched]["double"]

        win_amount = int(bet * multiplier)

        balance += win_amount

        wins += 1
        streak += 1

        biggest_win = max(biggest_win, win_amount)

        print("🎊 DOUBLE MATCH!")
        print(f"Multiplier : x{multiplier}")
        print(f"You Won ₹{win_amount}")

        result_text += f" | WIN ₹{win_amount}"

    else:

        losses += 1
        streak = 0

        print("❌ No Match")
        print(f"Lost ₹{bet}")

        result_text += f" | LOSS ₹{bet}"

    best_streak = max(best_streak, streak)
    highest_balance = max(highest_balance, balance)

    history.append(result_text)

    print(f"\n💰 Current Balance : ₹{balance}")

    # bonus

    if streak > 0 and streak % 5 == 0:

        balance += 100

        print("\n🎁 STREAK BONUS!")
        print("₹100 Added To Your Balance!")

# ================= MAIN LOOP ================= #

while True:

    print(f"""
╔════════════════════════════════════╗
║            🎮 MAIN MENU            ║
╠════════════════════════════════════╣
║ 💰 Balance : ₹{balance}
║ 🔥 Streak  : {streak}
╠════════════════════════════════════╣
║ 1. 🎰 Play
║ 2. 📊 Statistics
║ 3. 🚪 Exit
╚════════════════════════════════════╝
""")

    choice = input("Choose (1-3): ")

    if choice == "1":

        if balance <= 0:

            print("\n💀 GAME OVER")
            print("You are bankrupt!")

            break

        spin()

    elif choice == "2":

        show_stats()

    elif choice == "3":

        print(f"""
╔══════════════════════════════════════╗
║         👋 THANKS FOR PLAYING        ║
╠══════════════════════════════════════╣
║ 🎮 Games Played : {games_played}
║ 🏆 Wins         : {wins}
║ ❌ Losses       : {losses}
║ 🔥 Best Streak  : {best_streak}
║ 💰 Final Bal.   : ₹{balance}
║ 💎 Biggest Win  : ₹{biggest_win}
╚══════════════════════════════════════╝
""")
        break

    else:
        print("Invalid Choice.")
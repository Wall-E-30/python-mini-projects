import random 

user_wins = 0
bot_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose (Rock/Paper/Scissors or Quit): ").lower()
    if user_input == "quit":
        break
    if user_input not in options:
        print("\nEnter again")
        continue
    random_number = random.randint(0, 2)
    # rock=0, paper=1, scissors=2
    bot_choice = options[random_number]
    print("Bot choose", bot_choice + ".")

    if (user_input == "rock" and bot_choice == "scissors") or (user_input == "paper" and bot_choice == "rock") or (user_input == "scissors" and bot_choice == "paper"):
        print("You won!!!")
        user_wins += 1
    elif user_input == bot_choice:
        print("It's a tie.")
        continue
    else:
        print("Bot wins!")
        bot_wins += 1
print("You won", user_wins, "times.")
print("Bot won", bot_wins, "times.")
print("------End------")


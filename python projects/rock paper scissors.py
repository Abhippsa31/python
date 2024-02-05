import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user = input("Type rock/paper/scissors or 'q' to quit: ").lower()
    if user == "q":
        break

    if user not in options:
        continue

    random_no = random.randint(0, 2)
    computer_choose = options[random_no]
    print(f"Computer chose {computer_choose}.")

    if user == "rock" and computer_choose == "scissors":
        print("You won!")
        user_wins += 1
    elif user == "paper" and computer_choose == "rock":
        print("You won!")
        user_wins += 1
    elif user == "scissors" and computer_choose == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")

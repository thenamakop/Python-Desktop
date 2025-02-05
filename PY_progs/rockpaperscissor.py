import random

print("Rock Paper Scissor Game")
user = input("Enter your choice [ROCK, PAPER, SCISSOR] = ")

computer_choice = random.choice(["ROCK", "PAPER", "SCISSOR"])

if user == computer_choice:
    print("Match Tie")

elif user == "ROCK":
    if computer_choice == "PAPER":
        print("Computer won, Paper covers rock")
    else:
        print("You won, Rock smashes scissor")

elif user == "PAPER":
    if computer_choice == "ROCK":
        print("You won, Paper covers Rock")
    else:
        print("Computer won, scissor cuts paper")

elif user == "SCISSOR":
    if computer_choice == "ROCK":
        print("Computer won, rock smashesh scissor")
    else:
        print("You won, scissor cuts paper")

else:
    print("In-valid input")
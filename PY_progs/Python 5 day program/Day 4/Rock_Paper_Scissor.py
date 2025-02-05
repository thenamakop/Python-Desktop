'''python
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return

    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

play_game()
'''
import random
'''import random
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
    print("In-valid input")'''
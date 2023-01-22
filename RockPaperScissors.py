import random

# Define the options
options = ["rock", "paper", "scissors"]

# Prompt the user to make a choice
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Check if the user's choice is valid
if user_choice not in options:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    # Generate a random choice for the computer
    computer_choice = random.choice(options)

    # Compare the user's choice and the computer's choice
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose.")
#This code prompts the user to make a choice between "rock", "paper", or "scissors". It uses an if-else statement to check if the user's choice is valid, and if it is, it generates a random choice for the computer using the random.choice() function. It then uses another set of if-else statements to compare the user's choice and the computer's choice and determine the winner.
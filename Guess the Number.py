import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Keep prompting the user until they guess the number
while guess != number:
    if guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess a number between 1 and 10: "))

# Let the user know they guessed the number
print("You guessed the number! It was", number)
#This code uses the random module to generate a random number between 1 and 10. It then prompts the user to guess the number and uses a while loop to keep prompting the user until they guess the number correctly.

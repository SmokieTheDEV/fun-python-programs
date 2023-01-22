import random

# List of words to choose from
word_list = ["python", "program", "code", "computer"]

# Choose a random word from the list
word = random.choice(word_list)

# Convert the word to a list of characters
letters = list(word)

# Create a list of underscores the same length as the word
guessed_letters = ["_"] * len(letters)

# Loop until the word is guessed

import random
import string

# Get the desired length of the password from the user
length = int(input("Enter the desired length of the password: "))

# Get the characters to be included in the password from the user
characters = input("Enter the characters to be included in the password (e.g. a-z, A-Z, 0-9): ")

# Generate a random password
password = ''.join(random.choice(characters) for i in range(length))

# Print the password
print("The generated password is:", password)
#This code prompts the user to input the desired length of the password and the characters to be included in the password. It then uses the random.choice() function and a for loop to generate a random password of the desired length using the specified characters.

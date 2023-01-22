#This code prompts the user to input a noun, verb, and adjective, and then uses string concatenation to insert the user's input into a pre-written story.
# Prompt the user for input
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

# Insert the user's input into the story
story = "The " + adjective + " " + noun + " " + verb + " through the forest."

# Print the story
print(story)

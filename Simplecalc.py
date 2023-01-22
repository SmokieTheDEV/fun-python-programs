# Get the user's input
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

# Print the result
print(result)
#This code prompts the user to input two numbers and an operator, and then uses if-else statements to perform the corresponding arithmetic operation and store the result in a variable. It then prints the result.

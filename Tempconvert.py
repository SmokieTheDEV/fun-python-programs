# Get the temperature value and the unit from the user
temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (F for Fahrenheit or C for Celsius): ").upper()

# Convert the temperature
if unit == "F":
    celsius = (temp - 32) * 5/9
    print(temp, "Fahrenheit is", celsius, "Celsius.")
elif unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(temp, "Celsius is", fahrenheit, "Fahrenheit.")
else:
    print("Invalid unit.")
#This code prompts the user to input the temperature value and the unit of the temperature (F for Fahrenheit or C for Celsius). It then uses an if-else statement to convert the temperature and print the result.
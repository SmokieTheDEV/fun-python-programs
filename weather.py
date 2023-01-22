import requests

# Get the location from the user
location = input("Enter the location: ")

# Use the OpenWeatherMap API to get the current weather for the location
api_key = 'YOUR_API_KEY'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(location, api_key)
response = requests.get(url)

# Extract the data from the API response
data = response.json()

# Extract the main weather information
weather = data['weather'][0]['main']

# Extract the temperature information
temp = data['main']['temp']

# Print the weather and temperature information
print("The current weather in {} is: {}".format(location, weather))
print("The temperature is {:.2f}°C".format(temp - 273.15))

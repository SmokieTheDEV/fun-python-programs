import requests
from bs4 import BeautifulSoup

# Get the URL to be scraped from the user
url = input("Enter the URL to be scraped: ")

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information using the soup object
# for example, you can extract all the links in the page using the following command
links = soup.find_all('a')

# Print the extracted information
print(links)
#This code prompts the user to input the URL to be scraped, sends a GET request to the URL using the requests library, and then uses the BeautifulSoup library to parse the HTML content of the page and extract the desired information.

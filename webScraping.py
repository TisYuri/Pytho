# Import the required libraries
from bs4 import BeautifulSoup
import requests
import csv

# URL containing the data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

# Download the webpage
data = requests.get(url).text

# Create a BeautifulSoup object
soup = BeautifulSoup(data, "html.parser")

# Find the table in the webpage
table = soup.find('table')

# Prepare a list to store the data
scraped_data = []

# Loop through the rows of the table
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 2:  # Ensure the row has at least 2 columns
        language = cols[0].get_text()
        avg_salary = cols[1].get_text()
        scraped_data.append([language, avg_salary])

# Save the data into a CSV file
with open('popular-languages.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Programming Language", "Average Annual Salary"])
    # Write the scraped data
    writer.writerows(scraped_data)

print("Data has been saved to 'popular-languages.csv'")
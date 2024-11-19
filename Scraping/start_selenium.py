from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

#Note: chromedriver must be installed
#sudo apt-get install chromium-chromedriver
driver_path = '/usr/bin/chromedriver'
# Create a Service object
service = Service(driver_path)

# Initialize the WebDriver with the Service
driver = webdriver.Chrome(service=service)

# Open a website
driver.get('https://etfdb.com/screener/')

# Wait for the page to fully load
time.sleep(5)

# Get the page source and pass it to BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Close the browser
driver.quit()

# Use BeautifulSoup to extract data
#print(soup.prettify())

# Find all rows in the table
rows = soup.find_all('tr')

# Loop through the rows and extract the desired data
for row in rows:
    symbol_line = row.find('td', class_='screener-column-symbol')
    if symbol_line is None:
        continue
    symbol = symbol_line.text.strip()

    name_line = row.find('td', class_='screener-column-name')
    if name_line is None:
        continue
    name = name_line.text.strip()

    asset_line = row.find('td', class_='screener-column-asset-class')
    if asset_line is None:
        continue
    asset_class = asset_line.text.strip()

    # Print or store the extracted data
    print(f"Symbol: {symbol}, Name: {name}, Asset Class: {asset_class}")
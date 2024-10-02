from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Path to chromedriver
driver_path = '/usr/bin/chromedriver'
service = Service(driver_path)

# Initialize the WebDriver with the Service
driver = webdriver.Chrome(service=service)

page_num = 1  # Start from page 1

while True:
    # Construct the URL with the page number
    url = f'https://etfdb.com/screener/#page={page_num}'
    
    # Open the URL
    driver.get(url)
    
    try:
        # Wait until the table rows (<tr>) are present on the page, timeout after 10 seconds
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "tr"))
        )
    except Exception as e:
        print(f"Error or timeout on page {page_num}: {e}")
        break  # Exit the loop if the table rows are not found
    
    # Get the page source and pass it to BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all rows in the table
    rows = soup.find_all('tr')
    
    # Check if no data was found (i.e., an invalid page)
    if not rows:
        print(f"No data found on page {page_num}, stopping.")
        break  # Exit the loop if no rows are found
    
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
        print(f"Page {page_num} - Symbol: {symbol}, Name: {name}, Asset Class: {asset_class}")

    # Increment the page number for the next loop
    page_num += 1

# Close the browser
driver.quit()


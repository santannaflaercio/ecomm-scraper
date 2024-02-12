from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Webdriver configuration
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the page
driver.get("http://localhost:8000")

# Wait for dynamic content to load
time.sleep(1)

# Scrape the desired data
products = driver.find_elements(By.CSS_SELECTOR, "#products > h2")

for product in products:
    print(product.text)

# Close the browser
driver.quit()

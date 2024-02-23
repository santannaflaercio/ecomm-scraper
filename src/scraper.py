from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Use the ChromeDriver service to create a new WebDriver instance
with webdriver.Chrome(service=service) as driver:
    # Navigate to the target webpage
    driver.get("http://localhost:8000")

    # Wait until all elements with the CSS selector "#products > h2" are present on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#products > h2"))
    )

    # Find all elements with the CSS selector "#products > h2"
    products = driver.find_elements(By.CSS_SELECTOR, "#products > h2")

    # Print the text of each product element
    for product in products:
        print(product.text)


print("Scraping complete!")

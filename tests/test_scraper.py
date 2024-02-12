import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import subprocess


class ScraperTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the web server
        cls.server = subprocess.Popen(["python3", "-m", "http.server"], cwd="public/")

    @classmethod
    def tearDownClass(cls):
        # Stop the web server
        cls.server.kill()

    def setUp(self):
        # Webdriver configuration
        webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=webdriver_service)
        self.driver.get("http://localhost:8000")
        time.sleep(3)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_scrape_products(self):
        # Scrape the desired data
        products = self.driver.find_elements(By.CSS_SELECTOR, "#products > h2")
        product_texts = [product.text for product in products]
        expected_texts = ["Product 1", "Product 2", "Product 3"]
        self.assertEqual(product_texts, expected_texts)


if __name__ == "__main__":
    unittest.main()

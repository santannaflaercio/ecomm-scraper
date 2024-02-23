import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess


class ScraperTest(unittest.TestCase):
    """
    A test case for a web scraper, using Selenium WebDriver for browser automation.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case. This is where instance variables should be set.
        """
        super(ScraperTest, self).__init__(*args, **kwargs)
        self.server = None

    @classmethod
    def setUpClass(cls):
        """
        Set up the state for the test case. This method is called once before any tests or test cases are run.
        Here, it starts a web server in a subprocess.
        """
        cls.server = subprocess.Popen(
            ["python3", "-m", "http.server"], cwd="../public/"
        )

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the state for the test case. This method is called once after all tests or test cases have run.
        Here, it stops the web server that was started in setUpClass.
        """
        cls.server.kill()

    def setUp(self):
        """
        Set up the state for each test. This method is called before each individual test method is run.
        Here, it sets up a Selenium WebDriver and navigates to the local web server.
        """
        options = Options()
        options.add_argument("--headless")
        webdriver_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=webdriver_service)
        self.driver.get("http://localhost:8000")

    def tearDown(self):
        """
        Clean up the state after each test. This method is called after each individual test method has run.
        Here, it closes the Selenium WebDriver.
        """
        self.driver.quit()

    def test_scrape_products(self):
        """
        A test method. This is the actual test. It must start with the word 'test'.
        Here, it tests whether the web scraper can correctly scrape product names from the web page.
        """
        wait = WebDriverWait(self.driver, 10)
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#products > h2"))
        )
        product_texts = [product.text for product in products]
        expected_texts = ["Product 1", "Product 2", "Product 3"]
        self.assertEqual(product_texts, expected_texts)


if __name__ == "__main__":
    """
    This is the entry point for the script. It runs the test case if the script is run directly.
    """
    unittest.main()

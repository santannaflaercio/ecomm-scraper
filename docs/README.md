# Ecomm Scraper

This is a documentation file for the Ecomm Scraper project.

## Introduction

EcommScraper is a web scraping project designed to extract data from a fictitious e-commerce webpage that loads content dynamically. Here’s a detailed breakdown of how it operates:

1. **Initialization**: The script initiates a Selenium WebDriver and navigates to the local web page hosted at http://localhost:8000.

2. **Waiting for Content to Load**: As the webpage loads content dynamically, the script waits for a specific time (in this case, 3 seconds) to ensure all content is loaded.

3. **Data Extraction**: The script then scrapes the desired data from the page. In this case, it’s looking for h2 elements within an element with the ID products. It extracts the text from these elements, which represent the names of the products on the fictitious e-commerce page.

4. **Data Verification**: The script checks if the scraped data matches the expected data. This is done in a unit test method, which compares the scraped data with a list of expected product texts.

5. **Finalization**: After the data extraction and verification, the script closes the browser.

This project serves as a demonstration of how web scraping can be used to extract data from webpages that load content dynamically. It also showcases how unit tests can be used to verify the accuracy of the scraped data. Enjoy exploring EcommScraper!

## Installation

To install the Ecomm Scraper, follow these steps:

1. Clone the repository: `git clone https://github.com/santannaflaercio/ecomm-scraper.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the local server: `python -m http.server --directory public/ &`
4. Run the scraper: `python src/scraper.py`

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

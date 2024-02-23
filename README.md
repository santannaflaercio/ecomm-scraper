# E-commerce Scraper

![https://github.com/topics/python](https://img.shields.io/badge/Python-v3.10+-yellow)
![https://github.com/topics/captcha](https://img.shields.io/badge/Selenium-Scraper-blue)
![Status](https://img.shields.io/badge/Status-Complete-yellowgreen)

This repository contains a web scraping project designed to extract data from a fictitious e-commerce webpage that loads
content dynamically. The project uses Selenium WebDriver to navigate to the webpage, waits for the content to load,
scrapes the desired data, and verifies the accuracy of the scraped data using unit tests.

## What is Web Scraping?

Web scraping is the process of extracting data from webpages. It’s a powerful tool that can be used to gather
information from the internet, such as product prices, stock quotes, weather data, and more. Web scraping is often used
by businesses to collect data for market research, competitive analysis, and lead generation.

## Steps to Simulate a Web Scraper

As this project is a simulation, it doesn't actually scrape a real e-commerce webpage. Instead, it scrapes a local
webpage hosted at http://localhost:8000. Here’s a detailed breakdown of how the project operates:

1. **Initialization**: The script initiates a Selenium WebDriver and navigates to the local web page hosted
   at http://localhost:8000.

2. **Waiting for Content to Load**: As the webpage loads content dynamically, the script waits for a specific time (in
   this case, 3 seconds) to ensure all content is loaded.

3. **Data Extraction**: The script then scrapes the desired data from the page. In this case, it’s looking for h2
   elements within an element with the ID products. It extracts the text from these elements, which represent the names
   of the products on the fictitious e-commerce page.

4. **Unit Testing**: The script then verifies the accuracy of the scraped data using unit tests. It compares the
   extracted data with the expected data to ensure the scraper is working as intended.

## Project Structure

The project contains the following files:

- **`scraper.py`**: This script contains the web scraper. It uses Selenium WebDriver to navigate to the local web page,
  waits for the content to load, scrapes the desired data, and verifies the accuracy of the scraped data using unit
  tests.
- **`index.html`**: This file contains the HTML content of the local web page that the scraper navigates to. It contains
  a list of products that the scraper extracts data from.
- **`README.md`**: This file contains information about the project, how it works, and how to run it.

## How to Run the Scraper

To run the scraper, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/santannaflaercio/ecomm-scraper.git
    ```

2. Navigate to the project directory:

   ```bash
   cd ecomm-scraper
   ```

3. Install the required dependencies using the following command:

   ```bash
    pip install -r requirements.txt
    ```

4. Run the local web server using the following command:

   ```bash
   cd public/ && python -m http.server
   ```

   This command starts a local web server that hosts the `index.html` file at http://localhost:8000.

5. Run the scraper using the following command:

   ```bash
   python scraper.py
   ```

   If the scraper runs successfully, you should see the following output:

    ```bash
   Product 1
   Product 2
   Product 3
   Scraping complete!
    ```
   

## How to Contribute

Contributions are always welcome! Here's how you can get involved:

- Report any bugs or issues you encounter.
- Suggest new features or enhancements to improve the project.
- Submit pull requests with code improvements or fixes.

We appreciate your contributions and feedback to make this project better!

## License

This project is released without a license. You are free to use it for any purpose.

**Happy Scraping!**
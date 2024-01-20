# Address Data Scraper

## Overview
This script is designed to automate the process of scraping address data from a specified website. It utilizes the Selenium WebDriver for navigating the web pages and extracting the required information. The scraped data includes details such as district, neighborhood, street, building number, independent section, and geographical coordinates (longitude and latitude).

## Features
- Resumes scraping from the last point by reading the last row of the existing CSV file.
- Handles dynamic dropdowns for city (il), district (ilce), neighborhood (mahalle), street (CSBM), and building number (BINA NO).
- Handles reCAPTCHA if it appears during the scraping session.
- Stores the scraped data into a CSV file, appending new data to it.

## Requirements
- Python 3.x
- Selenium
- Pandas
- Chrome WebDriver (Make sure it's compatible with the installed Chrome version)

## Installation
1. Clone this repository or download the script.
2. Install the required Python packages:
    ```
    pip install selenium pandas
    ```
3. Download and set up the appropriate version of [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage
1. Ensure the Chrome WebDriver path is correctly set in the script or the system PATH.
2. Run the script:
    ```
    python main.py
    ```
3. The script will start scraping data and will automatically handle pagination and dropdowns.
4. The scraped data will be stored in `data/scraped_data.csv`.
5. To stop the script, press 'q' when prompted.

## Function Descriptions
- `read_last_row_from_csv(file_path)`: Reads the last row from the CSV file to determine where to resume scraping.
- `get_current_map_center()`: Retrieves the current center coordinates of the map view from the webpage.
- `append_to_csv(data, file_path)`: Appends the scraped data to the specified CSV file.
- `init_driver()`: Initializes the Selenium WebDriver with necessary options.
- `has_options(driver, select_id)`: Checks if a select element has options available.
- `main()`: Main function to control the flow of the script, including handling of reCAPTCHA, navigating dropdowns, and storing data.

## Note
- The script is designed to be resilient against website structure changes, specifically for dropdown handling and waiting for elements to be clickable or present.
- The script may require modifications if the website's structure or the CAPTCHA handling changes significantly.

## Contribution
Feel free to fork the project, make improvements, or adapt the script for other websites or purposes. Any contributions or suggestions are welcome!


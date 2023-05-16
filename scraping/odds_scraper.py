from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def scrape_odds(url):
    # Set up Chrome options to run the browser in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the Chrome driver executable path
    chrome_driver_path = r"C:\Users\eoina\Downloads\chromedriver_win32\chromedriver.exe"

    # Start the Chrome WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the ad to disappear
        wait = WebDriverWait(driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ad-selector")))

        # Find the table element
        table = driver.find_element(By.CSS_SELECTOR, ".eventTable")

        # Scrape the data from the table
        # TODO: Add your scraping logic here

    except TimeoutException:
        print("Timeout exception occurred.")

    finally:
        # Quit the driver
        driver.quit()

# URL of the page you want to scrape
url = "https://www.oddschecker.com/boxing"

# Call the function to scrape the odds
scrape_odds(url)

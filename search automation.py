from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Start the WebDriver and open Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open a webpage
    driver.get("https://www.google.com")

    # Step 2: Locate the search box and type a query
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()  # Submit instead of clicking the button

    # Step 3: Retrieve and print the title and URL of the results page
    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium WebDriver")
    )
    print("Title:", driver.title)
    print("URL:", driver.current_url)

    # Wait for a few seconds to view the results
    time.sleep(3)

finally:
    # Step 5: Close the browser
    driver.quit()

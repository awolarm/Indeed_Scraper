from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver executable (replace with your actual path)
chromedriver_path = './chromedriver'

# Set up ChromeDriver service
service = Service(executable_path=chromedriver_path)

# Initialize WebDriver with Chrome
driver = webdriver.Chrome(service=service)

try:
    # Navigate to a website
    driver.get('https://www.python.org')

    # Print the title of the page
    print(f"Page title: {driver.title}")

    # Take a screenshot
    driver.save_screenshot('python_website.png')

finally:
    # Always close the driver when done
    driver.quit()

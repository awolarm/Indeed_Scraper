from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up options to open the browser window
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Optional: start maximized

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

# Visit the URL
url = "https://www.chewy.com"
driver.get(url)

# Wait to view the page
time.sleep(10)  # Keep the window open for 60 seconds (adjust as needed)

# Optionally keep it open indefinitely until manually closed
# input("Press Enter to exit...")

driver.quit()  # Uncomment if you want to close automatically

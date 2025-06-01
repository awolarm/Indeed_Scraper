from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import selenium.webdriver
# this one works for finding random urls


def main():
    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")

    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    url = "https://www.chewy.com"
    print(f"Opening {url}...")
    driver.get(url)

    time.sleep(5)

    driver.quit()


if __name__ == "__main__":
    main()

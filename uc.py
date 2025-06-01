import undetected_chromedriver as uc
from multiprocessing import freeze_support
import time

# kinda works with uc


def main():
    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.get(
        'https://www.chewy.com')
    time.sleep(5)
    driver.save_screenshot('nowsecure.png')
    driver.quit()  # Don't forget to quit the driver when done


if __name__ == '__main__':
    freeze_support()  # This is necessary for multiprocessing on Windows
    main()

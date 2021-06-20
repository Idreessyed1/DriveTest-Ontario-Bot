import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scraper:

    def __init__(self, location, license_num, license_exp):
        self.PATH = "C:\Python_Projects\DriveTestBot\Resources\chromedriver.exe"
        self.URL = "https://drivetest.ca/book-a-road-test/booking.html#/verify-driver"
        self.license_num = license_num
        self.license_exp = license_exp
        self.location = location

        # Configuring driver
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        #options.headless = True

        # Running driver
        self.driver = webdriver.Chrome(self.PATH, options=options)
        self.driver.get(self.URL)

    def login(self):
        licence_number = self.driver.find_element_by_id("licenceNumber")
        licence_expiry_date = self.driver.find_element_by_id("licenceExpiryDate")
        licence_number.send_keys(self.license_num)
        licence_expiry_date.send_keys(self.license_exp)
        submit = self.driver.find_element_by_id("regSubmitBtn")
        submit.click()

    def reschedule(self):
        try:
            reschedule = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Reschedule Test")]'))
            )
            reschedule.click()
        except:
            print("Failed")

        try:
            reschedule_pop_up = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, '//button[@title="reschedule"]'))
            )
            reschedule_pop_up.click()
        except:
            print("Failed")

    def select_location(self):
        pass

    def schedule(self):
        pass

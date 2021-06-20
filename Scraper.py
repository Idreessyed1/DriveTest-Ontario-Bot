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
        self.wait = WebDriverWait(self.driver, 50)

    def login(self):
        licence_number = self.driver.find_element_by_id("licenceNumber")
        licence_expiry_date = self.driver.find_element_by_id("licenceExpiryDate")
        licence_number.send_keys(self.license_num)
        licence_expiry_date.send_keys(self.license_exp)
        submit = self.driver.find_element_by_id("regSubmitBtn")
        submit.click()

    def reschedule(self):
        reschedule = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Reschedule Test")]')))
        reschedule.click()
        reschedule_confirmation = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//button[@title="reschedule"]')))
        reschedule_confirmation.click()

    def select_location(self):
        location_selection = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//a[@title="' + self.location + '"]')))
        location_selection.click()
        location_submission = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="form-group loc-submit"]/'
                       'div[@class="directive_wrapper ng-isolate-scope"]/'
                       'button[@type="submit"]')))
        location_submission.click()

    def open_dates(self):
        open_dates = []
        time.sleep(1)
        for date in self.driver.find_elements_by_xpath('//td[@class="ng-scope"]'):
            if date.find_element_by_xpath('div/div/div').get_attribute('class') == "date-cell-contents":
                open_dates.append(date.text)
                print(date.text)

    def next_month(self):
        next_month_btn = self.driver.find_element_by_xpath('//a[@title="next month"]')
        next_month_btn.click()


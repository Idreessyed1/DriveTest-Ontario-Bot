import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True

PATH = "C:\Python_Projects\DriveTestBot\Resources\chromedriver.exe"
URL = "https://drivetest.ca/book-a-road-test/booking.html#/verify-driver"


driver = webdriver.Chrome(PATH)

driver.get(URL)
#print(driver.title)

# Logging in
licence_number = driver.find_element_by_id("licenceNumber")
licence_expiry_date = driver.find_element_by_id("licenceExpiryDate")
licence_number.send_keys("S9639-35760-10110")
licence_expiry_date.send_keys("2022/02/02")
submit = driver.find_element_by_id("regSubmitBtn")
submit.click()

#time.sleep(10)

try:
    reschedule = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Reschedule Test")]'))
    )
    reschedule.click()
except:
    print("Failed")

#modal = driver.find_element_by_css_selector("div.form-group lic-submit")
#modal = driver.find_element_by_xpath('//button[@class="btn btn-primary"][@title="reschedule"]')






# Rescheduling
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()

#time.sleep(3)

#driver.quit()

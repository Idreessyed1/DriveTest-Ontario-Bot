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
location = "Windsor"


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

try:
    reschedule_pop_up = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//button[@title="reschedule"]'))
    )
    reschedule_pop_up.click()
except:
    print("Failed")

#Reschedule pop-up
# reschedule_pop_up = driver.find_element_by_xpath('//button[@title="reschedule"]')
# reschedule_pop_up.click()

#Location selection
time.sleep(3)

#Test this first
# location_div = driver.find_element_by_class_name("dtc_listings")
# print(location_div.text)

try:
    location_selection = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//a[@title="' + location + '"]'))
    )
    location_selection.click()
except:
    print("Failed")


try:
    location_submission = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="form-group loc-submit"]/'
                       'div[@class="directive_wrapper ng-isolate-scope"]/'
                       'button[@type="submit"]'))
    )
    location_submission.click()
except:
    print("Failed")







# Rescheduling
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()

#time.sleep(3)

#driver.quit()

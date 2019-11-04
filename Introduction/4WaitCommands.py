import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner


# Synchronization: When we write selenium code, every statement will execute top to bottom. Implicit Waits & Explicit Waits.
driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")


# IMPLICIT WAIT 1) Waits for all elements to load

# Opening URL takes some time
driver.get("http://newtours.demoaut.com/")

# Wait some time here
driver.implicitly_wait(10) # seconds

# The following statement verifies whether this "statement" is in the title.
assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
"""

# EXPLICIT WAIT - 1) Applicable for all elelemts in the script 2) Will work basedon condition, not on time.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# Wait some time here
driver.implicitly_wait(5) # seconds

# Maximize the window()
driver.maximize_window()
driver.get("https://www.expedia.com")

driver.find_element_by_id("tab-flight-tab-hp").click()
#driver.find_element(By.ID, "tab-flight-tab-hp").click()
#driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']").click()

time.sleep(2) # from python

#driver.find_elements_by_id()
driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']").send_keys("NYC")
driver.find_element_by_xpath("//a[@id='aria-option-0']//div[1]").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']").clear
driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[@class='datepicker-cal-date'][contains(text(),'16')]").click()
driver.implicitly_wait(5)


driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']").click()
driver.implicitly_wait(5)
#driver.find_element_by_xpath("//div[3]//table[1]//tbody[1]//tr[2]//td[4]//button[1]")send_keys("10/11/2019")
#driver.find_element_by_xpath("//button[@class='datepicker-cal-date'][contains(text(),'19')]").click()
driver.find_element_by_xpath("//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']").click()
driver.find_element_by_xpath("//button[@class='datepicker-paging datepicker-next btn-paging btn-secondary next']").click()
driver.find_element_by_xpath("//div[@class='col gcw-date-field']//div[3]//table[1]//tbody[1]//tr[2]//td[5]//button[1]").click()

#returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
#returnDate.clear()
#returnDate.send_keys("12/26/2019")
driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']").click()

# Explicit Wait
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))


"""


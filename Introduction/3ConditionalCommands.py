# If we need to verify whether certain elements are displayed on the page or not.
# Whether we want to check whether certain check boxes have been selected or not.
# Download chromepath

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com/")

# Want to verify whether username textbox is displayed or not, and whether it is enabled or not.
ele1 = driver.find_element_by_name("userName")
# Returns True/False based of element status
print(ele1.is_displayed()) # returns T/F based of element status
print(ele1.is_enabled()) # returns T/F

# Want to verify whether username textbox is displayed or not, and whether it is enabled or not.
ele2 = driver.find_element_by_name("password")
# Returns True/False based of element status
print(ele2.is_displayed()) # returns T/F based of element status
print(ele2.is_enabled()) # returns T/F

ele1.send_keys("mercury")
ele2.send_keys("mercury")

#Clicking element by name
driver.find_element_by_name("login").click()
# Clicking element by xpath
# driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()

# Using CSS selector to find round trip
roundtrip_radio = driver.find_element_by_css_selector("input[value = roundtrip]")
print("Status of round trip: " + str(roundtrip_radio.is_selected()))

# Using CSS selector to find one way trip
onetrip_radio = driver.find_element_by_css_selector("input[value = oneway]")
print("Status of one-way trip: " + str(roundtrip_radio.is_selected()))
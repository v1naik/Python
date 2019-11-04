import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner

# How to find how many input boxes present in web page
# How to provide value in text box
# How to get the status of text box

# Selected or not isSelected()
# Checkbox & Radio Buttons

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
status = driver.find_element_by_xpath("//label[contains(text(),'Male')]").is_selected()
print(status)

driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
status = driver.find_element_by_xpath("//label[contains(text(),'Male')]").is_selected()
print(status)

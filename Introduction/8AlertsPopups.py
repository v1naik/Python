from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()

#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()


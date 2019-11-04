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
driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_id("RESULT_FileUpload-11").send_keys("/Users/vsnaik/Downloads/chromedriver")


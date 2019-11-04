import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

driver.save_screenshot("/Users/vsnaik/Downloads/homepage.jpg")
driver.get_screenshot_as_file("/Users/vsnaik/Downloads/homepage2.jpg")
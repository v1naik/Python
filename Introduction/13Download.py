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

chromeOptions = Options ()
#chromeOptions.add_experimental_option("prefs", ("download.default_directory":"Macbook/Users/vsnaik/Downloads/"))

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# Download Text File
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("testng download file")
driver.find_element_by_xpath("//button[@id='createTxt']").click()
driver.find_element_by_xpath("//a[@id='link-to-download']").click()

# Download PDF File
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver2")
driver.get("https://testautomationpractice.blogspot.com/")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

#Scroll down the Page by pixel
#driver.execute_script("window.scrollBy(0,500)","")

#Scroll down the page until element found
#flag = driver.find_element_by_xpath("//table[1]//tbody[1]//tr[86]//td[1]//img[1]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#Scroll to the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

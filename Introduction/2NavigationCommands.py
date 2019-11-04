import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver2")

driver.get("http://newtours.demoaut.com/")
print(driver.title) #FR

driver.get("http://pavantestingtools.blogspot.in")
#time.sleep(5)  Navigation takes times. This allows stalling. Put some waiting times.
print(driver.title) #TT

driver.back()
#time.sleep(5)
print(driver.title) #FR

driver.forward()
#time.sleep(5)
print(driver.title) #TT
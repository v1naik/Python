import openpyxl
import DDT.XLUtils

from selenium import webdriver
path = "/Users/vsnaik/PycharmProjects/Selenium/Login.xlsx"
driver = webdriver.Chrome(executable_path="/Users/vsnaik/Downloads/chromedriver")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

rows = DDT.XLUtils.getRowCount(path, "Sheet1")

#r represents row number
for r in range(2,rows+1):
    username = DDT.XLUtils.readData(path, "Sheet1", r, 1)
    password = DDT.XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("//input[@name='userName']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='login']").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test is passed")
        DDT.XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test failed!")
        DDT.XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element_by_link_text("Home").click()


import openpyxl
import DDT.XLUtils

from selenium import webdriver
path = "/Users/vsnaik/PycharmProjects/Selenium/DDT/Login2.xlsx"
driver = webdriver.Chrome(executable_path="/Users/vsnaik/Downloads/chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

rows = DDT.XLUtils.getRowCount(path, "Sheet1")

links = driver.find_elements_by_tag_name("a")
print ("Number of links present: ", len(links))

#r represents row number
for r in range(2,rows+1):
    username = DDT.XLUtils.readData(path, "Sheet1", r, 1)
    password = DDT.XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys(password)
    driver.find_element_by_xpath("//input[@id='btnLogin']").click()

    if driver.title == "OrangeHRM":
        print("Test is passed")
        DDT.XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
        print("Number of links present: ", len(links))

        '''
        driver.find_element_by_xpath("//a[@id='welcome']").click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        '''
    else:
        print("Test failed!")
        DDT.XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest
from AutomationFramework1.Pages.loginPage import LoginPage
from AutomationFramework1.Pages.homePage import homePage
import AutomationFramework1.Utils.XLUtils

class LoginTests(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/vsnaik/Downloads/chromedriver")
        self.path = "/Users/vsnaik/PycharmProjects/Selenium/DDT/Login2.xlsx"
        self.rows = AutomationFramework1.Utils.XLUtils.getRowCount(self.path, "Sheet1")
        self.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver
        #driver.get("https://opensource-demo.orangehrmlive.com/")
        #links = driver.find_elements_by_tag_name("a")
        #print("Number of links present: ", len(links))


        for r in range(2, self.rows + 1):
            driver.get("https://opensource-demo.orangehrmlive.com/")
            links = driver.find_elements_by_tag_name("a")
            username = AutomationFramework1.Utils.XLUtils.readData(self.path, "Sheet1", r, 1)
            password = AutomationFramework1.Utils.XLUtils.readData(self.path, "Sheet1", r, 2)

            login = LoginPage(driver)
            login.enter_username(username)
            login.enter_password(password)
            login.click_login()

            if links != 6:
                AutomationFramework1.Utils.XLUtils.writeData(self.path, "Sheet1", r, 3, "Test Passed")
                homepage = homePage(driver)
                time.sleep(10)
                homepage.click_welcome()
                homepage.click_logout()
                time.sleep(10)
            else:
                print("Test failed!")
                AutomationFramework1.Utils.XLUtils.writeData(self.path, "Sheet1", r, 3, "Test Failed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()

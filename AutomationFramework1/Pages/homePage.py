class homePage():

    def  __init__(self, driver):
        self.driver = driver

        # These are the 3 locators on this page.
        self.welcome_link_xpath = "//a[@id='welcome']"
        self.logout_link_xpath = "//a[contains(text(),'Logout')]"

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
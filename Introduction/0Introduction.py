import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
# Example 1
# Creating Driver Object
driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")

# Go to the following website
driver.get("http://newtours.demoaut.com")

# Returns Title of the page
print(driver.title)

# Capture the current url of the page
print(driver.current_url)

# Close the browser
driver.close()


# Example 2 (Way 1)
# Creating Driver Object
driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.set_page_load_timeout(10)
driver.maximize_window()

driver.get("https://www.google.com/")
driver.find_element_by_xpath("//input[@name='q']").send_keys("Automation")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@class='VlcLAe']//input[@name='btnK']").click()

time.sleep(2)
driver.close()
driver.quit()

print("Test Completed")


# Example 2
# Creating Driver Object
driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.set_page_load_timeout(10)
driver.maximize_window()

driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Automation")
driver.find_element_by_name("btnk").click()

time.sleep(2)
driver.close()
driver.quit()

print("Test Completed")



class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by Name")

ff = FindByIdName()
ff.test()


class FindByXPathCSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByCss = driver.find_element_by_css_selector("#displayed-text")

        if elementByCss is not None:
            print("We found an element by CSS")

ff = FindByXPathCSS()
ff.test()

"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver)

# Copy Xpath of the element. Make sure to put single quotes
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# To use the following command you have to import time package.
time.sleep(5)

# The parent window closes, but the child window is still open. Close command only closes one browser at a time
driver.close()

# This command closes all the windows
driver.quit()

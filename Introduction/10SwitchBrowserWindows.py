from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

#driver.maximize_window()

driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()
print (driver.current_window_handle) #CDwindow-FA0D8D5E8DE5E0DA8DF4338FAB480313

handles = driver.window_handles # Returns all handle values of opened browser windows


for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)

    if driver.title == "Frames & windows":
        driver.close() # close only parent browser


#driver.quit() Close all browsers

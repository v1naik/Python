from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com")

links = driver.find_elements_by_tag_name("a")
print ("Number of links present: ", len(links))

for link in links:
    print(link.text)

driver.find_element_by_partial_link_text("REG").click()
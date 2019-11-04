from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")

"""
#Mouse Hover
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("// input[ @ id = 'txtUsername']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
usermgmt = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
"""
"""
#Double Click
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element = driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")
actions = ActionChains(driver)
actions.double_click(element).perform() #Double-click on the button
"""
"""
#Right-Click
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/div[1]/p[1]/span[1]")
#button = driver.find_element_by_xpath("//a[contains(text(),'jQuery Context Menu Demo Gallery')]")
actions = ActionChains(driver)
actions.context_click(button).perform()
"""

"""
#Drag-and-Drop
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element_by_xpath("//div[@id='DHTMLgoodies_dragableElement0']")
target_element = driver.find_element_by_xpath("//div[@id='box106']")
actions = ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()
"""
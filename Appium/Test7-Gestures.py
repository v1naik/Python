import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

"""
DESIRED CAPABILITIES
"""
desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "appPackage": "com.android.contacts",
  "appActivity": "com.android.contacts.activities.PeopleActivity",
  "newcommandTimeout": 600
}

# Create the Driver Instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Allow app to access device data
# for i in range(4):
   # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
   # time.sleep(2)

# AUTOMATING MOBILE GESTURES
user_action = TouchAction(driver)
# Add ID - Coordinates x=960,y=1676. Tap on the Add icon
user_action.tap(x=960,y=1676).perform()

# Hit Cancel
driver.find_element_by_id("com.android.contacts:id/left_button").click()
time.sleep(3)

# Tap Phone, More Fields
# driver.find_element_by_id("android:id/text1").click()
driver.find_element_by_id("com.android.contacts:id/more_fields").click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='More fields']").click()

#Scroll Down and Up
time.sleep(5)
user_action.press().move_to().release().perform()
time.sleep(5)
user_action.press().move_to().release().perform()
time.sleep(5)

#Long Press and Add name
name = driver.find_element_by_xpath("")
name.send_keys("Appium Widget")
time.sleep(3)
user_action.long_press(name, duration=3000).perform()

#Hide Keyboard
driver.hide_keyboard()


"""
Interact with list of elements
Mobile options_xpath: //android.widget.CheckedTextView[@text='Mobile']

# TO DO
list_of_values = driver.find_elements_by_xpath("//android.widget.CheckedTextView[@resource-id='android:id/text1']")
print(len(list_of_values)]

expected_list = ['Mobile', 'Home', 'Work', 'Work Fax', 'Home Fax', 'Pager', 'Other']
actual_list = []

for value in list_of_values:
  ele_name = value.get_attribute("text")
  print(ele_name)
  actual_list.append(ele_name)
  
print(actual_list)

assert expected_list == actual_list, "The list did not match"
"""
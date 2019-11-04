from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/Users/vsnaik/Downloads/flipkart.apk",
  "appPackage": "",
  "appWaitActivity": ""
}

# Create the Driver Instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Add Implicit Wait
driver.implicitly_wait(30)

# Close the window using ID
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

# Get the price of the first laptop and verify the price
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
driver.implicitly_wait(30)
# Make up your own xpath or take direct xpath
driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,630][360,885]']").click()
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()



#Touch Actions

#TouchAction(driver)   .press(x=801, y=1490)   .move_to(x=828, y=720)   .release()   .perform()

#Swipe Once
touch = TouchAction(driver)
touch.press(x=801, y=1490).move_to(x=828, y=720).release().perform()

"""
#Swipe multiple times
for i in range(5):
    touch = TouchAction(driver)
    touch.press(x=801, y=1490).move_to(x=801, y=720).release().perform()
    time.sleep(3)

"""
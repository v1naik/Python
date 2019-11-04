import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

"""
DESIRED CAPABILITIES
"""
desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/Users/vsnaik/Downloads/flipkart.apk",
  "appPackage": "",
  "appWaitActivity": ""
}

# Create the Driver Instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Close the window using ID
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

"""
Taking Screenshots and Storing it with Current Activity and Timestamp

    @ driver methods
        - current activity
        - save screenshot

    @ Python methods/properties
        - strftime
"""

ts = (time.strftime("%Y_%m_%d_%H%M%S"))
activityname = driver.current_activity
filename = activityname+ts

driver.save_screenshot("/Users/vsnaik/Downloads/" + filename + ".png")
driver.sa

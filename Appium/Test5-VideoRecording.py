import base64
import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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

"""
Video Recording

    @ driver methods
        -start_recording_screen()
        -stop_recording_screen()

    @ Python
        -convert Base-64 into media (mp4) file

    @ steps:
        1) Convert filepath (using os.path.join (directory, filename))
        2) Save the video base64 file from stop recording method
        3) Convert base64 into media file (mp4) using with <expression> as <variable>: decode base file
"""

# Start Video Recording
driver.start_recording_screen()

# Close the window using ID
driver.implicitly_wait(30)
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

video_rawdata = driver.stop_recording_screen()

"""
# Get the price of the first laptop and verify the price
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,1650][360,1794]']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,846][540,1614]']").click()
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()
"""

#video_rawdata = driver.stop_recording_screen()

video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

# ENABLE HIDDEN FILES
filepath = os.path.join("/Users/vsnaik/Downloads/", video_name + ".mp4")
with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
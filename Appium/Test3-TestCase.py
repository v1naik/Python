from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/Users/vsnaik/Downloads/flipkart.apk",
  "appPackage": "",
  "appWaitActivity": ""
}

# Create the Driver Instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Open bash profile: touch ~/.bash_profile; open ~/.bash_profile
# Add the following: export PATH=$PATH:/PATH/TO/android-sdk-macosx/build-tools/x.x.x
# Then: aapt d --values badging /Users/vsnaik/Downloads/flipkart.apk
# Locate: package, launchable-activity to get appPackage & appWaitActivity
# App info is another way

# Add Implicit Wait
driver.implicitly_wait(30)

# Close the window using ID
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()

# Get the price of the first laptop and verify the price
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Drawer']").click()
driver.implicitly_wait(30)

# Make up your own xpath or take direct xpath
driver.find_element_by_xpath("//android.widget.TextView[@text='Electronics']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,1650][360,1794]']").click()
driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,846][540,1614]']").click()

driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

price = driver.find_element_by_xpath("//android.widget.TextView[@bounds='[297,629][388,678]']").get_attribute("text")

print ("The price value is: " + price)

assert price == "₹279", "The price has not matched"


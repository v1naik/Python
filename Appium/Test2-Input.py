from appium import webdriver
#com.flipkart.android_6.10-970350_minAPI16(x86)(nodpi)_apkmirror.com.apk
desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/Users/vsnaik/Downloads/flipkart.apk",
  "appPackage": "com.flipkart.android",
  "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
}

# Create the Driver Instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# Add Implicit Wait
driver.implicitly_wait(30)


# Close the window using ID
driver.find_element_by_id("com.flipkart.android:id/btn_skip").click()


# Click the search box, then type Iphone (Using Xpath)
driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Search on flipkart"]/android.widget.TextView').click()
driver.find_element_by_xpath('//android.widget.EditText[@content-desc="Search grocery products in Supermart"]').send_keys("Iphone")
driver.implicitly_wait(30)

# Click the search box, then type Iphone (Using ID)
# driver.find_element_by_id("com.flipkart.android:id/search_widget_textbox").click()
# driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView").send_keys("Iphone")
# driver.implicitly_wait(30)

# Another Way
# search_element = driver.find_element_by_id("com.flipkart.android:id/search_autoCompleteTextView")
# driver.set_value(search_element, "Iphone")


# go, search, send, next, done, previous
driver.execute_script('mobile: performEditorAction', {'action':'search'})


"""
#Locate the Not Now
driver.find_element_by_id("com.flipkart.android:id/not_now_button").click()

# Another Way
# popBtn = driver.find_element_by_class_name("android.widget.Button")
# driver.set_value(popBtn, "NOT NOW")

"""
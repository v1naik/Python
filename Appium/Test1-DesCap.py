from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "/Users/vsnaik/Downloads/AirMirror Remote support Remote control devices_v1.0.4.3_apkpure.com.apk",
  "appPackage": "com.sand.airmirror",
  "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)



# AirMirror Remote support Remote control devices_v1.0.4.3_apkpure.com.apk
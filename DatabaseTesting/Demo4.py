import time
import pymysql
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("http://newtours.demoaut.com")
driver.maximize_window()

# CONNECT TO DATABASE
db = pymysql.connect("localhost","root","NmiSM2P","UserAccounts" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
query1 = "SELECT * FROM Account1"

cursor.execute(query1)

for cols in cursor:
    #print(cols[0], "    ", cols[1], "         ", cols[2])
    driver.find_element_by_xpath("//input[@name='userName']").send_keys(cols[0])
    driver.find_element_by_xpath("//input[@name='password']").send_keys(cols[1])
    driver.find_element_by_xpath("//input[@name='login']").click()
    time.sleep(5)

    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test Passed")
    else:
        print("Test Failed")
    driver.find_element_by_xpath("//a[contains(text(),'Home')]").click()


cursor.close()
db.commit()
db.close()

print("Data Driven Test Completed")
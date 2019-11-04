from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path = "/Users/vsnaik/Downloads/chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_xpath("//select[@id='RESULT_RadioButton-9']")
drp = Select(element)

#   Select by Visible text
# drp.select_by_visible_text("Morning") #Morning

#   Select by Index
# drp.select_by_index(2)  #Afternoon

#   Count number of options
print(len(drp.options))

#   Capture all the options and print them as output
all_options = drp.options

for option in all_options:
    print(option.text)






import time

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_down_country=driver.find_element(By.XPATH, "//*[@id='country']")
Country=Select(drop_down_country)

# -------------BY USING SELENIUM SELECT CLASS WE CAN SELECT THE OPTION IN 3 WAYS-----------------

#Country.select_by_visible_text("France") By using select_by_visible_text() method..

#Country.select_by_value("india") By using select_by_value() method..

#Country.select_by_index(5) # By using select_by_index() method..


# -------------WITHOUT USING SELENIUM SELECT METHOD------------------
allOpt=Country.options
for option in allOpt:
    if option.text=="Australia":
        option.click()
        break
  
 #for option in Country.options: same as above
   # print(len(Country.options)) 10

   #print(option.text)

    #print(option.get_attribute("value"))
  
    

input("Press Enter to close browser...")
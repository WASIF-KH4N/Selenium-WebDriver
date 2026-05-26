

from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Select Specific Checkbox
#checkbox1=driver.find_element(By.XPATH, "//*[@id='sunday']")
#checkbox1.click()

# Select All Checkboxes
#checkbox2=driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")
#checkbox2.click()   error
'''print(len(checkbox2)) # 7
for checkbox in checkbox2:
    checkbox.click()'''

#Select some checkboxes
#checkbox3=driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")
# For example, to select the first and third checkboxes:
#checkbox3[0].click()
#checkbox3[2].click()

'''for checkbox in checkbox3:
    weakname=checkbox.get_attribute("id")
    if weakname=="monday" or weakname=="saturday":
        checkbox.click()'''

# Select the last two checkboxes
'''checkbox4=driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")
for checkbox in range(len(checkbox4)-2,len(checkbox4)):
    checkbox4[checkbox].click()'''

# Select the first four checkboxes
'''checkbox5=driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")
for checkbox in range(len(checkbox5)):
    if checkbox <4:
        checkbox5[checkbox].click() '''


#Unselect all checkboxes
checkbox6=driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id,'day')]")

for checkbox in checkbox6:
  if checkbox.is_selected():
    checkbox.click()
    

input("Press Enter to close browser...")


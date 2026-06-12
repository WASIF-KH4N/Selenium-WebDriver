from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://saucedemo.com/")

#----------------------FIND-ELEMENT
username=driver.find_element(By.XPATH,"//*[@id='user-name']")
username.send_keys("standard_user")
print(len(username)) # object of type 'WebElement' has no len()
print(username.text) # empty string

#----------------------FIND-ELEMENTS
password=driver.find_elements(By.XPATH,"//*[@id='password']")
password[0].send_keys("secret_sauce")
print(len(password)) 
print(password[0].text) # empty string
input("Test complete. Press Enter to close browser...")
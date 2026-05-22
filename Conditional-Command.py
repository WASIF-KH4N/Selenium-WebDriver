from selenium import webdriver
from selenium.webdriver.common.by import By     
driver=webdriver.Edge()
driver.get("https://orangehrm.com/contact-sales")
driver.maximize_window()
name=driver.find_element(By.XPATH, "//*[@id='Form_getForm_FullName']")
name.send_keys("Selenium")
#button=driver.find_element(By.XPATH, "//*[@id='headingSolutions']/button")
button=driver.find_element(By.XPATH, "/html/body/nav/div/div/div/div/div[1]/div[2]/h2/button")
#button=driver.find_element(By.XPATH, "//*[@id='Form_getForm_action_submitForm']")
checkbox=driver.find_element(By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")
print("Name is visible:", name.is_displayed())
print("Name is enabled:", name.is_enabled())
print("Button is visible:", button.is_displayed())
print("Button is enabled:", button.is_enabled())

print("Checkbox is selected:", checkbox.is_selected())
print("Checkbox is clicked")
checkbox.click()
print("Checkbox is selected:", checkbox.is_selected())

'''
driver.get("https://admin-demo.nopcommerce.com/login")    
check=driver.find_element(By.XPATH, "//*[@id='RememberMe']")
print("Checkbox is visible:", check.is_displayed())
print("Checkbox is enabled:", check.is_enabled())   
print("Checkbox is selected:", check.is_selected()) 

print("After Click the checkbox...")
check.click()
print("Checkbox is selected:", check.is_selected()) '''


input("Press Enter to close browser...")

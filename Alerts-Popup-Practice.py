import time

from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(7)
alertwindow=driver.switch_to.alert  
print(alertwindow.text)
alertwindow.send_keys("Selenium Practice")
alertwindow.accept()
#alertwindow.dismiss()


'''driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()

alertwindow=driver.switch_to.alert
print(alertwindow.text) 
alertwindow.accept()
#alertwindow.dismiss()'''




#----Authentication pop-up----
#driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#driver.maximize_window()



input("Press Enter to close browser...")
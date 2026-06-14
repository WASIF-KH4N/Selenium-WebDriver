from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
driver.maximize_window()

doubleClick=driver.find_element(By.ID, "doubleClickBtn")
rightClick=driver.find_element(By.ID, "rightClickBtn")

acts=webdriver.ActionChains(driver)

acts.double_click(doubleClick).perform() # double click on button
acts.context_click(rightClick).perform() # right click on button

input("Press Enter to close the browser...")
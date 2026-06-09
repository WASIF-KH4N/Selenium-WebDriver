from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.new_window('tab') #Opens new tab in same browser window

#driver.switch_to.new_window('window') #Opens new browser window

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

input("Press Enter to close browser...")


from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://automationexercise.com/")
driver.get("https://saucedemo.com/")
driver.back()
driver.forward()
driver.refresh()
input("Press Enter to close browser...")
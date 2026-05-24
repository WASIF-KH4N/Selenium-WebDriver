import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
#time.sleep(5) by using time.sleep(), performace of script is poor..
driver.implicitly_wait(5) # It will apply in all elements of the script..

driver.get("https://www.opencart.com/")


driver.find_element(By.LINK_TEXT, "FEATURES").click()

input(" Press Enter to close browser...")
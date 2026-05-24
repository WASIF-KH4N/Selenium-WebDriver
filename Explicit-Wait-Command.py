
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,Exception])

driver.get("https://www.opencart.com/")

#Explicit Wait based on conditions and it is applied for specific element only, not for all elements of the script.
feature_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "FEATURES")))
feature_link.click()


demo_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "DEMO")))
demo_link.click()

input(" Press Enter to close browser...")
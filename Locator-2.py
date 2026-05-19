from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://automationexercise.com/")
driver.maximize_window()
#Absolut/full XPATH
driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a").click()

#Relative/partial XPATH
driver.find_element(By.XPATH, "//*[@id='search_product']").send_keys("Men Tshirt")
driver.find_element(By.XPATH, "//*[@id='submit_search']").click()
#driver.find_element(By.XPATH, "//a[@data-product-id='28' and @class='btn ']").click()
#driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
#driver.find_element(By.XPATH, "//*[contains(@data-product-id,'2')]").click()
driver.find_element(By.XPATH, "//*[contains(@class,'cart')]").click()



input("Test complete. Press Enter to close browser...")

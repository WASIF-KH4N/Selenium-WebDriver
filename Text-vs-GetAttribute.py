from attrs import field
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://automationexercise.com/products")
driver.maximize_window()

input_field=driver.find_element(By.XPATH, "//*[@id='search_product']")
input_field.send_keys("jeans")

#button=driver.find_element(By.ID, "submit_search")
#button.click()

cart =driver.find_element(By.LINK_TEXT, "Cart")
print("Cart is", cart.text) # Cart
print("Cart is", cart.get_attribute("href")) # https://automationexercise.com/view_cart

print("input is",input_field.text) # empty string

print("input is",input_field.get_attribute("value")) # jeans
print("input is",input_field.get_attribute("type")) # text

input("Press Enter to close browser...")
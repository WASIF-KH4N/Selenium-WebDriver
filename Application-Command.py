

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.get("https://orangehrm.com/contact-sales")
#driver.get("https://admin-demo.nopcommerce.com/Admin/Discount/List")
driver.maximize_window()
email=driver.find_element(By.XPATH,"//*[@id='Email']")
email.clear()
email.send_keys(" admin@yourstore.com")
password=driver.find_element(By.XPATH,"//*[@id='Password']")
password.clear()
password.send_keys("admin")
driver.find_element(By.XPATH, "//*[@id='main']/div/section/div/div[2]/div[1]/div/form/div[3]/button").click()
print(driver.title)
print(driver.current_url)
print(driver.page_source)

input("Press Enter to close browser...")
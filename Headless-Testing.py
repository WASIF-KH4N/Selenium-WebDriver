from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_argument("--headless") #Run browser in headless mode (without GUI)
#opts.add_argument("--headless=new") #Recommended hai for better stability

driver=webdriver.Chrome(options=opts)
driver.get("https://www.saucedemo.com/")


driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//*[@id='login-button']").click()

print(driver.title)
print(driver.current_url)

#checking login is sucessful or not by verifying URL of page after login
if "inventory.html" in driver.current_url:
    print("Login successful")
else:
    print("Login failed")
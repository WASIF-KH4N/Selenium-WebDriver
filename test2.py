'''from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Test passed")
else:
    print("Test failed")
input("Test complete. Press Enter to close browser...")
'''
#driver.close()
#------------------------------------------------------------------------------------------------------------------


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)

# wait for username field
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

# FIX: use CSS selector instead of CLASS_NAME
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#login_btn = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login_btn.click()

# wait for dashboard/title change
wait.until(EC.title_contains("OrangeHRM"))

act_title = driver.title
exp_title = "OrangeHRM"

if exp_title in act_title:
    print("Test passed")
else:
    print("Test failed")

input("Test complete. Press Enter to close browser...")
driver.quit()



#----------------------------------------------------------------------------------------------------------------------



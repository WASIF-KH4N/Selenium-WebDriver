from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc"))
)

link.click()

#input("Press Enter to close browser...")
#driver.close()
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
serv =Service(r"C:\Program Files\Python314\Scripts\chromedriver.exe")
driver=webdriver.Chrome(service=serv)
#driver.get("https://www.facebook.com")
#driver.get("https://www.opencart.com/")
#driver.get("http://automationpractice.com/index.php")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
wait = WebDriverWait(driver, 10)
about = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn[data-test=continue-shopping]"))
)
about.click()
driver.find_element(By.CSS_SELECTOR, "Button.btn").click()
driver.find_element(By.CLASS_NAME, "product_sort_container").click()

about = wait.until(
    EC.element_to_be_clickable((driver.find_element(By.ID,"react-burger-menu-btn")))
)
about.click()
#driver.find_element(By.LINK_TEXT, "About").click()
#wait = WebDriverWait(driver, 30)

'''about = wait.until(
    #EC.element_to_be_clickable((By.LINK_TEXT, "About"))
    #EC.element_to_be_clickable((By.CSS_SELECTOR,"a[data-test=about-sidebar-link]"))
    #EC.element_to_be_clickable((By.CSS_SELECTOR, "a#about_sidebar_link"))
    #EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id=about_sidebar_link]"))
    #EC.element_to_be_clickable((By.ID, "about_sidebar_link"))

)

about.click()'''
a=driver.find_elements(By.CLASS_NAME, "inventory_item")
print(len(a))
b=driver.find_elements(By.TAG_NAME, "a")
print(len(b))
#driver.find_element(By.ID, "about_sidebar_link").click()
input("Test complete. Press Enter to close browser...")


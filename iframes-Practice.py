from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Edge()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

Outer_frame=driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(Outer_frame) #iframe doesnot have id or name attribute thats why i use web element to switch the frame..

Inner_frame=driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(Inner_frame) #iframe doesnot have id or name attribute thats why i use web element to switch the frame..


driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("WASIF")

driver.switch_to.parent_frame() # Switch to outer frame from inner frame..

input("Press Enter to close the browser...")    
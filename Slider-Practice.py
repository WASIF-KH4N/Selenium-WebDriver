from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")

# switch into the demo iframe that contains the slider
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
Slider=driver.find_element(By.XPATH,"//*[@id='slider']/span")
print("Position of slide before moving",Slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(Slider,300,0).perform() # drag and drop by offset (x,y)

print("Position of slider after moving",Slider.location) # location is used to get the position of element in x and y coordinates

'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

min_slider=driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider=driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

acts=ActionChains(driver)
acts.drag_and_drop_by_offset(min_slider, 30, 0).perform() 
acts.drag_and_drop_by_offset(max_slider, -50, 0).perform() 

input("Press Enter to close the browser...")
'''
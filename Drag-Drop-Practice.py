from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get("https://www.learnaqa.info/drag-and-drop/")
driver.maximize_window()

source1=driver.find_element(By.XPATH,"//*[@id='item-1']")
source1=driver.find_element(By.XPATH,"//*[@id='item-2']")

destination1=driver.find_element(By.XPATH,"//*[@id='drop-zone']")

acts1=ActionChains(driver)

acts1.drag_and_drop(source1, destination1).perform() # drag and drop source to destination
#acts1.drag_and_drop(source2, destination1).perform() # drag and drop source to destination

input("Press Enter to close the browser...")
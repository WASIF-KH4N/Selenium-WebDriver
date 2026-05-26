
#This pop up comes from browser not from the webpage. It is called browser pop up.

from selenium import webdriver
from selenium.webdriver.common.by import By 

opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")

driver=webdriver.Chrome(options=opt)   
driver.get("https://whatmylocation.com/")

input("Press Enter to close the browser...")            
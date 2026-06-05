from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/all-countries.html")
driver.maximize_window()

#Approach 1:
driver.execute_script("window.scrollTo(0, 1000)") # scroll down by 1000 pixels
value=driver.execute_script("return window.pageYOffset;") # get the current scroll position
print("Current scroll position is: ", value)


#Approach 2: 
flag=driver.find_element(By.XPATH,"//*[@id='ct-list']/ul[2]/li[69]")
driver.execute_script("arguments[0].scrollIntoView();", flag) 
value=driver.execute_script("return window.pageYOffset;") 
print("Current scroll position is: ", value)


#Approach 3:
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)") # scroll to the bottom of the page
value=driver.execute_script("return window.pageYOffset;") # get the current scroll position
print("Current scroll position is from top to bottom: ", value)

#scroll to the top of the page
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)") # scroll to the bottom of the page
value=driver.execute_script("return window.pageYOffset;") # get the current scroll position
print("Current scroll position is from bottom to top: ", value)


input("Press Enter to close the browser...")
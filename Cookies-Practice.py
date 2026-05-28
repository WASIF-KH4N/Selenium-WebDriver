from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.opencart.com/")
driver.maximize_window()

cookies = driver.get_cookies() #Capture cookies from browser
print("Size of cookies before adding new cookie:", len(cookies)) #Print size of cookies

driver.add_cookie({"name": "MyCookie", "value": "123456"}) #Add new cookie to browser
driver.add_cookie({"name": "MyCookie2", "value": "abcdef"}) #Add another cookie to browser

cookies = driver.get_cookies() 

print("Size of cookies after adding new cookie:", len(cookies)) #Print size of cookies again after adding new cookie 

driver.delete_cookie("MyCookie2") #Delete specific cookie from browser using cookie name

cookies = driver.get_cookies() 
print("Size of cookies after deleting cookie:", len(cookies)) #Print size of cookies after deleting one cookie 

driver.delete_all_cookies() #Delete all cookies from browser
cookies = driver.get_cookies()

print("Size of cookies after deleting all cookies:", len(cookies)) #Print size of cookies after deleting all cookies
#print("Size of cookies:", len(cookies)) dynamically get size of cookies Eg-> 6,7,8.....

for cookie in cookies:
    #print(cookie) #Print all cookies in dictionary format
    #print(cookie.get("name"),":",cookie.get("value")) #Print only cookie names and values

  input("Press Enter to close browser...")
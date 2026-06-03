
# ======IDENTIFYING THE NORMSL LINKS AND BROKEN LINKS IN THE WEBPAGE=======

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Edge()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME, "a")  # by using tagname.....
count=0;  # by using tagname.....
#print("Total links:", len(links)) 48

for link in links:
    url=link.get_attribute("href")
    try:
        response=requests.head(url)
    except:
        None
    response=requests.head(url)
    if response.status_code >= 400:
        print("URL is a broken link:", url)
        count=count+1
    else:
        print("URL is a valid link:", url)

print("Total broken links:", count)

input("Press Enter to close browser...")


'''from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#driver.find_element(By.PARTIAL_LINK_TEXT,"dem").click()
driver.find_element(By.LINK_TEXT, "Udemy Courses").click()

#links=driver.find_elements(By.TAG_NAME, "a")  # by using tagname.....
links=driver.find_elements(By.XPATH, "//a") # by using xpath.....

print("Total links:", len(links)) #78

for link in links:
    print(link.text) # it will print all the links text which are present in the webpage.
    print(link.get_attribute("href")) # it will print all the links which are present in the webpage.

input("Press Enter to close browser...")'''
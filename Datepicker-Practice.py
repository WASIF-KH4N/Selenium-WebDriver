
from selenium import webdriver
from selenium.webdriver.common.by import By         
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# 99% work this method 
#driver.switch_to.frame(0) # switch to frame by index
#driver.find_element(By.ID,"datepicker").send_keys("06/11/2002")

#But if .send_keys() method is not working so we can write logic for manually selecting from datepicker........

driver.switch_to.frame(0) 
year="2025"
month="December"
date="11"

driver.find_element(By.ID,"datepicker").click()


while True:
    mon=driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    yr=driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if mon==month and yr==year:
        break
    else:
        #driver.find_element(By.XPATH, "//*[@id=\"ui-datepicker-div\"]/div/a[2]/span").click() # click on next button
        driver.find_element(By.XPATH, "//*[@id=\"ui-datepicker-div\"]/div/a[1]/span").click() # click on previous button


dates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a") 
for ele in dates:
    if ele.text==date:
        ele.click()
        break

input("Press Enter to close browser...")



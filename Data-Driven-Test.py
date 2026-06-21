import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import ExcelUtility

driver=webdriver.Chrome()
driver.get("https://fd-calculator.com/")
driver.maximize_window()

   #Read data from Excel
file="C:\\Users\\PMLS\\Desktop\\Selenium\\depositData.xlsx"
rows = ExcelUtility.getRowCount(file, "Sheet1")
    
for r in range(2, rows+1):
    Amount = ExcelUtility.readData(file, "Sheet1", r, 1)
    RateInterest = ExcelUtility.readData(file, "Sheet1", r, 2)
    PeriodDuration = ExcelUtility.readData(file, "Sheet1", r, 3)
    PeriodType = ExcelUtility.readData(file, "Sheet1", r, 4)
    Frequency = ExcelUtility.readData(file, "Sheet1", r, 5)
    Expected_MaturityValue = ExcelUtility.readData(file, "Sheet1", r, 6)
    time.sleep(2)

    #Passing data to the Website
    amount = driver.find_element(By.XPATH,"//input[@id='fd-amount']")
    amount.clear()
    amount.send_keys(Amount)

    rate = driver.find_element(By.XPATH,"//input[@id='interest-rate']")
    rate.clear()
    rate.send_keys(RateInterest)

    period = driver.find_element(By.XPATH,"//input[@id='fd-period']")
    period.clear()
    period.send_keys(PeriodDuration)

    selectType = Select(driver.find_element(By.XPATH,"//select[@id='fd-period-type']"))
    selectType.select_by_visible_text(PeriodType)
    selectFrequency = Select(driver.find_element(By.XPATH,"//select[@id='compounding-frequency']"))
    selectFrequency.select_by_visible_text(Frequency)
    driver.find_element(By.XPATH,"//button[@id='calculate-btn']").click()
    #Actual_MaturityValue = driver.find_element(By.XPATH, "//*[@id='result']").text
    Actual_MaturityValue = driver.find_element(By.XPATH, "//div[@id='result']//b").text
    
    Actual_MaturityValue = Actual_MaturityValue.replace("₹", "")
    Actual_MaturityValue = Actual_MaturityValue.replace(",", "")
    Actual_MaturityValue = Actual_MaturityValue.strip() #Remove Extra spaces
    
    #Validation 
    if float(Expected_MaturityValue)==float(Actual_MaturityValue):
        print("Test Passed")
        ExcelUtility.writeData(file, "Sheet1", r, 8, "Passed")
        ExcelUtility.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("Test Failed")
        ExcelUtility.writeData(file, "Sheet1", r, 8, "Failed")
        ExcelUtility.fillRedColor(file, "Sheet1", r, 8)

input("Press Enter to continue...")











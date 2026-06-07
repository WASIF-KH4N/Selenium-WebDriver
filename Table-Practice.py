from selenium import webdriver
from selenium.webdriver.common.by import By 
driver=webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#--------------------------Count number of rows and columns in the table--------------------------
RowCount = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print("Number of rows in the table:", RowCount)
ColumnCount = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th[1]"))
print("Number of columns in the table:", ColumnCount)


#--------------------------Read specific row and column --------------------------
'''specificRow=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]").text
print("Specific Row is:", specificRow)
specificColumn=driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[1]")
for column in specificColumn:
    print(column.text)


specificElement=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[5]").text
print(specificElement) #Java --> 3rd row and 3rd column '''

#--------------------------Read all the data from the table--------------------------
'''specificRow=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
specificColumn=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
for allData in range(2, specificRow+1):
    for allColumn in range(1, specificColumn+1):
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(allData)+"]/td["+str(allColumn)+"]").text
        print(data, end="     ")
    print() # for new line after each row   '''


#--------------------------Read data based on conditions--------------------------
#----------To print the book name and price whose author name is Mukesh-----------

'''specificRow=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
for allData in range(2, specificRow+1):
    authorName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(allData)+"]/td[2]").text
    if authorName=="Mukesh":
       bookName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(allData)+"]/td[1]").text
       price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(allData)+"]/td[4]").text
       print(bookName,"  ",authorName,"  ",price)
    '''


input("Press Enter to close the browser...")
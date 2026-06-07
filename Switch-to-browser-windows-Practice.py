from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)

link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc"))
)

link.click()
 #
# Print ID of One window
#winID1=driver.current_window_handle
#print("Current Window ID is", winID1)

#------------------------------------APPROACH 1--------------------------------------
# Print IDs of all windows
#winIDS=driver.window_handles
#winID1=winIDS[0]
#winID2=winIDS[1]

#print("First Window ID: ", winID1, "Second Window ID: ", winID2)
#OR
#Print("All Window IDs are", winIDS) 

'''driver.switch_to.window(winID2)
print("Title of Second/Child Window is", driver.title)

driver.switch_to.window(winID1)
print("Title of First/Parent Window is", driver.title)

input("Press Enter to close browser...")'''


#------------------------------------APPROACH 2--------------------------------------

#wait.until(EC.number_of_windows_to_be(2))
'''winIDS=driver.window_handles
for winID in winIDS:
    driver.switch_to.window(winID)
    print(driver.title)'''


#-------------------------CLOSE SPECIFIC BROWSER WINDOW---------------------------

'''WinIDS=driver.window_handles
for winID in WinIDS:
    driver.switch_to.window(winID)
    if driver.title=="OrangeHRM: All in One HR Software for Businesses | OrangeHRM":
        break'''

input("Press Enter to close browser...")
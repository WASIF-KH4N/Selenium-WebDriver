from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH, "//*[@id='billname']").send_keys("John Doe")
#driver.save_screenshot('Dummy ticket.png')
driver.save_screenshot("C:\\Users\\PMLS\\Downloads\\Dummy ticket.png")
driver.get_screenshot_as_file("ticket.jpeg")
driver.maximize_window()

input("Press Enter to close browser...")
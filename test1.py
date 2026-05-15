
from selenium import webdriver
#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)

# Open Chrome browser
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")

# Get page title
title = driver.title

# Verify title
if "Google" in title:
    print("Test Passed")
else:
    print("Test Failed")
input("Test complete. Press Enter to close browser...")    



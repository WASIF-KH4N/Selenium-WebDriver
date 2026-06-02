
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/menu#")
driver.maximize_window()

actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

# Main menu
main_item = wait.until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Main Item 2"))
)

# Hover on Main Item 2
actions.move_to_element(main_item).perform()

# Now submenu becomes visible
sub_item = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[contains(text(),'SUB SUB LIST')]")
    )
)

# Hover on submenu
actions.move_to_element(sub_item).perform()

# Final item
inside_sub_item = wait.until(
    EC.visibility_of_element_located(
        (By.LINK_TEXT, "Sub Sub Item 1")
    )
)

# Click final item
actions.move_to_element(inside_sub_item).click().perform()

input("Press Enter to close browser...")
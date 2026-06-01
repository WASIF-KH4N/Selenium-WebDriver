from selenium import webdriver

from selenium.webdriver.common.by import By 

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://text-compare.com/")

driver.maximize_window()

textarea1=driver.find_element(By.XPATH,"//*[@id='inputText1']")

textarea2=driver.find_element(By.XPATH,"//*[@id='inputText2']")

textarea1.send_keys("SQA ENGINEER")

act=webdriver.ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform() # select all text

act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform() # copy text

act.send_keys(Keys.TAB).perform() # move to next text area

act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # paste text

input("Press Enter to close the browser...")
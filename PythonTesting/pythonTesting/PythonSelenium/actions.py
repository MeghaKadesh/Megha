import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https:rahulshettyacademy.com/AutomationPractice")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.double_click(driver.find_element(By).perform()
#action.context_click()
#action.drag_and_drop()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).perform()
time.sleep(5)
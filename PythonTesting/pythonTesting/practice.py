from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://int.zigzag.lk/collections/blazers-jackets")
driver.find_element(By.XPATH,"//label[@for='Filter-Style size-1'][span]").click()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://int.zigzag.lk/collections/blazers-jackets")
driver.find_element(By.XPATH,"//label[@for='Filter-Style size-1'][span]").click()
driver.find_element(By.ID,"URl")
driver.find_element(By.CSS_SELECTOR,"#url")

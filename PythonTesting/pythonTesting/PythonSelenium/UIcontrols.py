import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
check = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(check))
for checkbox in check:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        #assert checkbox.is_selected()
        break


radio = driver.find_elements(By.CSS_SELECTOR,"input[name='radioButton']")
print(len(radio))
for radiobutton in radio:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        break

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()



time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.find_element(By.CSS_SELECTOR,"input[name='enter-name']").send_keys("Megha")
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
a = driver.switch_to.alert        # to switch webdrive to alter mood
altertext1 = a.text
print(altertext1)
assert "Megha" in altertext1
a.accept()                         # to accepting the alter mood
#a.dismiss()                       # to dismiss the alter mood
time.sleep(5)
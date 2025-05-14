#locators
#ID name classname linkText CssSelector  Xpath
#Xpath sytax:
#//tagname[@attribute='value']
#CSSSelector syntax:
# tagname[attribute='value]       #ID    .ClassName
#using text : syntax is:    //tagname[text()='name of the text']


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME,"email").send_keys("meha@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123345")
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Megha")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Dhaduti")
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success!" in message

time.sleep(10)
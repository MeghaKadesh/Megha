#two types of dropdowns
#1: Static DropDown: Options in the dropdowns are fixed.
#use select class for static dropdown :Systex: a = select(findelement(By."value")
#if we have select tag in html code .. blindly use select tag for dropdown
#a.select_BY_visible_text
#a.select_BY_index
#a.select_By_value
#2:Dynamic or auto suggestive dropdowns: based on input ,options will display
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.NAME,"email").send_keys("meha@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123345")
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Megha")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
#dropdown.select_by_value("")
dropdown.select_by_visible_text("Female")
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Dhaduti")
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success!" in message

time.sleep(10)


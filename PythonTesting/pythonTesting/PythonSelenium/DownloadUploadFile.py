from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
fruit_name = "Apple"
fileUpload="C:\\Users\\kades\\Downloads\\download.xlsx"
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,"downloadButton").click()

file = driver.find_element(By.XPATH,"//input[@type='file']")
file.send_keys(fileUpload)

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[text()='Updated Excel Data Successfully.']")))
print(driver.find_element(By.XPATH,"//div[text()='Updated Excel Data Successfully.']").text)

price = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_fruit = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price+"-undefined']").text
print(actual_fruit)

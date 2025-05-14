from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()
name_phones = driver.find_elements(By.XPATH,"//div[@class='card h-100']")       # or //a[contains(@href,'shop')] this is also xpath
for names in name_phones:
    productName = names.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        names.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CSS_SELECTOR,"div[class*='checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
summary = driver.find_element(By.CSS_SELECTOR,".alert-success").text
assert "Thank you!" in summary




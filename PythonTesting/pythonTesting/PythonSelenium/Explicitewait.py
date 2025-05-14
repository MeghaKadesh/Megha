import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expectedlist =['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList =[]
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
veggies = driver.find_elements(By.XPATH,"//div[@class='products'] /div")
print(len(veggies))
for vegg in veggies:
    vegg.find_element(By.XPATH,"div/button").click()
    actualList.append(vegg.find_element(By.XPATH,"h4").text)
assert actualList==expectedlist
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
abc = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(abc)

totalvegg = driver.find_elements(By.CSS_SELECTOR,".quantity")
sum1=0
for totalveggies in totalvegg:
    sum1=sum1+int(totalveggies.text)
print(sum1)
totalamt = driver.find_elements(By.XPATH,"//td[5]/p")
sum2 = 0
for totalamts in totalamt:
    sum2= sum2+ int(totalamts.text)
print(sum2)
total = int (driver.find_element(By.CSS_SELECTOR,".totAmt").text)

discount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert total > discount
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()











from selenium import webdriver
from selenium.webdriver.common.by import By

browserSorted = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#driver.find_element(By.XPATH,"//a[@href='#/offers']").click()
# click on veggies list
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
#collect all the browserveggiList into one list
veggiesWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
print(len(veggiesWebElements))
for veggies in veggiesWebElements:
    browserSorted.append(veggies.text)


OriginalBrowserSortedList = browserSorted.copy()
print(OriginalBrowserSortedList)
#sort this compare
browserSorted.sort()
assert browserSorted == OriginalBrowserSortedList





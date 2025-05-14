from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles          # it is for which window to open...that we have metion in the next line bricket
driver.switch_to.window(windowsOpened[1])      # to switch perent window to child window
abc = driver.find_element(By.TAG_NAME,"h3").text
print(abc)
driver.close()

driver.switch_to.window(windowsOpened[0])
xyz = driver.find_element(By.TAG_NAME,"h3").text
print(xyz)
assert "Opening a new window" == xyz

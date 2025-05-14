from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")              # executing in headless mood
driver = webdriver.Chrome(options = chrome_options)

chrome_options.add_argument("--ignore-certificate-errors")         # ignoring all certificate errors while opening the browser.


driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")       # exicution ofjava script code using python javascript code
driver.get_screenshot_as_file("screen.png")               # to take screenshoot

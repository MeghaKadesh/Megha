from selenium.webdriver.common.by import By


class LoginPagePractice:
    def __init__(self,driver):
        self.driver = driver
        self.loginUser = (By.ID, "username")
        self.passwordUser = (By.XPATH, "//input[@type='password']")
        self.loginButton = (By.ID, "signInBtn")



    def loginPage1(self,userName,password):
        self.driver.find_element(*self.loginUser).send_keys(userName)
        self.driver.find_element(*self.passwordUser).send_keys(password)
        self.driver.find_element(*self.loginButton).click()

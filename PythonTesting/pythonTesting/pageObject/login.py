from selenium.webdriver.common.by import By

from pageObject.shop import ShopPage
from utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.user_name = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signinButton = (By.ID, "signInBtn")



    def login(self,username,password):
        self.driver.find_element(*self.user_name).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signinButton).click()
        shop_page = ShopPage(self.driver)
        return shop_page




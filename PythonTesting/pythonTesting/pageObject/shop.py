from selenium.webdriver.common.by import By

from pageObject.checkout import CheckOut_Page
from utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shopButton = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cart = (By.XPATH, "//div[@class='card h-100']")
        self.check_out = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_to_cart(self,product_Name):
        self.driver.find_element(*self.shopButton).click()
        name_phones = self.driver.find_elements(*self.product_cart)  # or //a[contains(@href,'shop')] this is also xpath
        for names in name_phones:
            productName = names.find_element(By.XPATH, "div/h4/a").text
            if productName == "product_Name":
                names.find_element(By.XPATH, "div/button").click()


    def go_cart(self):
        self.driver.find_element(*self.check_out).click()
        check_out = CheckOut_Page(self.driver)
        return check_out

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.BrowserUtils import BrowserUtils


class CheckOut_Page(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.check_button = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country = (By.ID, "country")
        #self.country_option = (By.LINK_TEXT, "India")
        self.country_select = (By.LINK_TEXT, "India")
        self.checkbox = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
        self.success_button = (By.CSS_SELECTOR, ".btn-success")
        self.alter_message = (By.CSS_SELECTOR, ".alert ")



    def check_out_button(self):
        self.driver.find_element(*self.check_button).click()




    def delivery_address(self,countryName):
        self.driver.find_element(*self.country).send_keys(countryName)

        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(self.country_select))
        self.driver.find_element(*self.country_select).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.success_button).click()



    def validate_order(self):
        abc = self.driver.find_element(*self.alter_message).text
        assert " Thank you!" in abc


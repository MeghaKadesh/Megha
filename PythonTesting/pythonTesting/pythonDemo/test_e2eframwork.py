import json
import os
import sys

import pytest


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.login import  LoginPage
#from pageObject.checkout import CheckOut_Page
#from pageObject.shop import ShopPage


path_name ='../data/test_e2eframwork.json'
with open (path_name) as f:
    test_object = json.load(f)
    test_name = test_object["data"]


@pytest.mark.parametrize("test_use",test_name)
def test_e2e(browserIntanse,test_use):
    driver = browserIntanse


    login_page = LoginPage(driver)
    print(login_page.getTitle())
    shop_page = login_page.login(test_use["user_name"],test_use["password"])


    shop_page.add_to_cart(test_use["productName"])
    print(shop_page.getTitle())
    check_out = shop_page.go_cart()


    check_out.check_out_button()
    check_out.delivery_address(test_use["delivery_address"])
    check_out.validate_order()











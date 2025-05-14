import json
import os
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pageObject.loginpage_practice import LoginPagePractice

path_name = '../data/test_endToendframework.json'
with open (path_name) as f:
    test_objectName = json.load(f)
    test_dataUse = test_objectName["data"]

@pytest.mark.parametrize("test_use",test_dataUse)

def test_practice_endToend(browserInstances12,test_use):
    driver = browserInstances12

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPageWork = LoginPagePractice(driver)
    loginPageWork.loginPage1(test_use["userName"],test_use["password"])






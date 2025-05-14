import os

import pytest
from selenium import webdriver
driver = None


@pytest.fixture(scope="class")
def setup():
    print("i'm printing first")
    yield
    print("I'm megha")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Megha", "Dhaduti", "megha@gmail.com"]

@pytest.fixture(params = ["chrome","Firefox", "IS"])
def browser(request):
    return request.param

@pytest.fixture(params= [("Megha","Dhaduti","123"), ("kadesh","guledagudda","234"),("love","to","infinity")])
def Love_To(request):
    return request.param





def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserIntanse(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
     driver = webdriver.Chrome()

    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(7)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    yield driver
    driver.close()







def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Firefox", help="browser selection for end to end testing"
    )




@pytest.fixture(scope="function")
def browserInstances12(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()

    elif browser_name == "Firefox":
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    yield driver
    driver.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
         Extends the Pytest Plugin to take and embed screenshot in html report, whenever testCase fail
         :param item:

         """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra',[])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__),'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::","_")+".png")
            print("file name is" + file_name)
            _capture_screenshot(file_name)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;'\
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)









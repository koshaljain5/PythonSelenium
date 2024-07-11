import pytest
from selenium import webdriver
from utilities import ReadConfigurations


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    global driver
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide valid browser")

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(ReadConfigurations.read_configurations("basic info", "url"))
    request.cls.driver = driver
    yield
    driver.quit()
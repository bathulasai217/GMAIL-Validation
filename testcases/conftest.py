import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



@pytest.fixture()
def setup(request,browser):
    if browser == "edge":
        serv_obj = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "chrome":
        serv_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=serv_obj)
    else:
        ser_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://www.gmail.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


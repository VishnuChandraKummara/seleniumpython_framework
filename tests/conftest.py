import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("browser_name")

    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="F://Tech//Softwares//Browser_drivers//chromedriver.exe")
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path="F://Tech//Softwares//Browser_drivers//geckodriver.exe")
    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="F://Tech//Softwares//Browser_drivers//msedgedriver.exe")
    elif browsername == "ie":
        driver = webdriver.Ie(executable_path="F://Tech//Softwares//Browser_drivers//IEDriverServer.exe")

    driver.get("http://rahulshettyacademy.com//angularpractice")
    driver.maximize_window()
    request.cls.driver = driver
    
    yield
    driver.close()
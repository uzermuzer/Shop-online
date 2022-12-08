import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.Chrome import GeckoDriverManager

@pytest.fixture(scope="session")
def browser():
    print('\nstart browser for test..')
    service_obj = Service("c:\/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    yield driver
    driver.quit()
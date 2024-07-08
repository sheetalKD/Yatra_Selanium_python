import time

import pytest
from selenium import webdriver
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    time.sleep(2)
    yield
    driver.close()

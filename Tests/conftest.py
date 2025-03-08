import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Utility import reader_config

import random
var=random.uniform(1.0,1000.0)
@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    options = Options()
    options.add_argument("--incognito")  # Start the browser in incognito mode
    options.add_argument("--start-maximized")  # Maximized the browser window
    options.add_experimental_option("excludeSwitches", [
        "enable-automation"])# Disable the infobar for chrome is bing controlled by automated software
    options.add_argument("--disable-notifications")
    url= reader_config.config_reader("basic info", "url")
    user= reader_config.config_reader("basic info", "Username")
    password = reader_config.config_reader("basic info", "Password")
    global driver
    driver=webdriver.Chrome(options)
    driver.get(url)
    request.cls.driver=driver
    request.cls.user=user
    request.cls.password=password
    yield driver
    allure.attach(driver.get_screenshot_as_png(),name=f"scr{var}",attachment_type=AttachmentType.PNG)
    driver.quit()